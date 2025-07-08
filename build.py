#!/usr/bin/env python3
"""
build.py - Python workflow for building PDFs and HTML from Jupyter notebooks and Jupyter Book.

- Reads notebooks.yaml for notebook list
- Calls update_toc.sh to sync _toc.yml
- Builds PDFs (only if needed) using nbconvert
- Builds full book PDF and HTML using Jupyter Book
- Copies/moves outputs to _build/latex and _build/html
- Gives clear output and errors

Usage:
    python build.py [--pdf] [--html]
    (default: both)
"""

import argparse
import subprocess
import sys
import os
import shutil
import yaml
from pathlib import Path
import re

def run_or_exit(cmd, **kwargs):
    """
    Run a subprocess command, print it, and exit on failure.
    Returns the CompletedProcess object.
    """
    print(f"[RUN] {' '.join(str(x) for x in cmd)}")
    try:
        result = subprocess.run(cmd, **kwargs)
    except Exception as e:
        print(f"[ERROR] Exception running command: {e}", file=sys.stderr)
        sys.exit(1)
    if result.returncode != 0:
        print(f"[ERROR] Command failed with exit code {result.returncode}: {' '.join(str(x) for x in cmd)}", file=sys.stderr)
        if hasattr(result, 'stderr') and result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    return result

def parse_yaml_list(yaml_path):
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    # Expect a top-level list or dict with a key like 'notebooks'
    if isinstance(data, dict) and 'notebooks' in data:
        return [n for n in data['notebooks'] if n and not str(n).startswith('#')]
    elif isinstance(data, list):
        return [n for n in data if n and not str(n).startswith('#')]
    else:
        raise ValueError(f"Unexpected YAML structure in {yaml_path}")

def main():

    import requests
    import contextlib
    import shutil
    from pathlib import Path  # Ensure Path is always imported in main()

    parser = argparse.ArgumentParser(description="Build PDFs, Markdown, DOCX, HTML, custom web output, or just collect all images from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
    parser.add_argument('--md', action='store_true', help='Build Markdown only')
    parser.add_argument('--docx', action='store_true', help='Build DOCX only')
    parser.add_argument('--latex', action='store_true', help='Build LaTeX only')
    parser.add_argument('--html', action='store_true', help='Build HTML (calls build-web.py)')
    parser.add_argument('--img', action='store_true', help='Collect all referenced images into _build/images/')
    parser.add_argument('--all', action='store_true', help='Build all formats: LaTeX, PDF, Markdown, DOCX, and HTML web output')
    parser.add_argument('--files', nargs='+', help='One or more notebook files to build (relative to notebooks/ or absolute)')
    parser.add_argument('--jupyter', action='store_true', help='Build a unified Jupyter Notebook in _build/jupyter and copy to docs/jupyter')
    args = parser.parse_args()

    # --- Unified Jupyter Book HTML Build ---
    if getattr(args, 'jupyter', False):
        repo_root = Path(__file__).parent.resolve()
        build_jupyter_dir = repo_root / '_build/jupyter'
        docs_jupyter_dir = repo_root / 'docs/jupyter'
        build_jupyter_dir.mkdir(parents=True, exist_ok=True)
        docs_jupyter_dir.mkdir(parents=True, exist_ok=True)
        # Build the Jupyter Book HTML site into _build/jupyter
        print(f"[INFO] Building Jupyter Book HTML into {build_jupyter_dir} ...")
        jb_cmd = ["jupyter-book", "build", str(repo_root), "--path-output", str(build_jupyter_dir)]
        print(f"[DEBUG] Running command: {' '.join(jb_cmd)}")
        result = run_or_exit(jb_cmd, capture_output=True, text=True)
        print("[DEBUG] jupyter-book stdout:\n" + (result.stdout or ""))
        print("[DEBUG] jupyter-book stderr:\n" + (result.stderr or ""))
        # Copy the built HTML site to docs/jupyter (replace contents)
        html_out = build_jupyter_dir / '_build' / 'html'
        if not html_out.exists():
            print(f"[ERROR] Expected HTML output not found at {html_out}")
            sys.exit(1)
        for item in docs_jupyter_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        for item in html_out.iterdir():
            dest = docs_jupyter_dir / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)
        print(f"[INFO] Jupyter Book HTML site copied to {docs_jupyter_dir}")
        return

    # --- HTML Build Option: just call build-web.py --html (and pass --files if given) ---
    if getattr(args, 'html', False):
        cmd = [sys.executable, str(Path(__file__).parent / 'build-web.py'), '--html']
        if args.files:
            cmd += ['--files'] + args.files
        print(f"[INFO] Calling build-web.py: {' '.join(cmd)}")
        run_or_exit(cmd)
        return

    # Directories and image search roots (must be set before any logic or function that uses them)
    repo_root = Path(__file__).parent.resolve()
    build_dir = repo_root / '_build'
    build_dir.mkdir(parents=True, exist_ok=True)  # Ensure _build exists
    chapters_dir = build_dir / 'tex'
    html_dir = build_dir / 'html'
    # notebook_dir is no longer used for notebook path construction
    # Use _notebooks.yaml instead of notebooks.yaml
    notebooks_yaml = repo_root / '_notebooks.yaml'
    update_toc = repo_root / 'scripts' / 'update_toc.sh'
    images_root_candidates = [repo_root / 'images', repo_root / 'content/images']

    # --- Build Images Only ---
    # Only run this block if --img is set, and return after
    if getattr(args, 'img', False):
        img_dir = build_dir / 'images'
        img_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Collecting all images referenced in notebooks and markdown into {img_dir}")
        def process_file_for_images(file_path, nb_stem=None):
            from fetch_youtube import fetch_youtube_thumbnail
            if not file_path.exists():
                print(f"[WARN] File not found: {file_path}")
                return
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            img_links = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
            img_links += re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', content)
            for img_path in set(img_links):
                yt_match = re.match(r'https?://img\.youtube\.com/vi/([\w-]{11})/', img_path)
                if yt_match:
                    video_id = yt_match.group(1)
                    flat_name = f"{nb_stem}_youtube_{video_id}.jpg" if nb_stem else f"youtube_{video_id}.jpg"
                    dst_img = img_dir / flat_name
                    if fetch_youtube_thumbnail(video_id, dst_img):
                        print(f"[IMG] Downloaded YouTube thumbnail for {video_id} to {dst_img}")
                    else:
                        print(f"[WARN] Could not fetch YouTube thumbnail for {video_id}")
                    continue
                if img_path.startswith('http'):
                    img_filename = os.path.basename(img_path.split('?')[0])
                    flat_name = f"{nb_stem}_{img_filename}" if nb_stem else img_filename
                    dst_img = img_dir / flat_name
                    try:
                        resp = requests.get(img_path, timeout=15)
                        if resp.status_code == 200:
                            with open(dst_img, 'wb') as outimg:
                                outimg.write(resp.content)
                            print(f"[IMG] Downloaded remote image {img_path} to {dst_img}")
                        else:
                            print(f"[WARN] Failed to download image {img_path}: HTTP {resp.status_code}")
                    except Exception as e:
                        print(f"[WARN] Could not download image {img_path}: {e}")
                    continue
                found = False
                real_img_path = None
                img_filename = os.path.basename(img_path)
                if not os.path.isabs(img_path) and not img_path.startswith('~'):
                    candidate = (file_path.parent / img_path).resolve()
                    if candidate.exists():
                        real_img_path = candidate
                        found = True
                if not found:
                    for images_root in images_root_candidates:
                        norm_img_path = os.path.normpath(img_path).lstrip(os.sep)
                        candidate = images_root / norm_img_path
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                if not found:
                    for images_root in images_root_candidates:
                        candidate = images_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                for fallback_root in [repo_root / 'content/notebooks/_images', repo_root / '_images']:
                    if not found:
                        candidate = fallback_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                if not found:
                    html_img_root = repo_root / '_build/html/images'
                    candidate = html_img_root / img_filename
                    if candidate.exists():
                        real_img_path = candidate
                        found = True
                    if not found:
                        for subdir, _, files in os.walk(html_img_root):
                            if img_filename in files:
                                real_img_path = Path(subdir) / img_filename
                                found = True
                                break
                if not found and os.path.dirname(img_path):
                    norm_img_path = os.path.normpath(img_path).lstrip(os.sep)
                    for images_root in images_root_candidates:
                        for subdir, _, files in os.walk(images_root):
                            candidate = Path(subdir) / Path(norm_img_path)
                            if candidate.exists():
                                real_img_path = candidate
                                found = True
                                break
                        if found:
                            break
                if not found:
                    for images_root in images_root_candidates:
                        for subdir, _, files in os.walk(images_root):
                            if img_filename in files:
                                real_img_path = Path(subdir) / img_filename
                                found = True
                                break
                        if found:
                            break
                if found and real_img_path:
                    flat_name = f"{nb_stem}_{img_filename}" if nb_stem else img_filename
                    dst_img = img_dir / flat_name
                    try:
                        shutil.copy2(real_img_path, dst_img)
                        print(f"[IMG] Copied {img_path} from {real_img_path} to {dst_img}")
                    except Exception as e:
                        print(f"[WARN] Could not copy image {real_img_path} to {dst_img}: {e}")
                else:
                    print(f"[WARN] Could not find image: {img_path}")
        if args.files:
            notebooks = []
            for f in args.files:
                nb_path = Path(f)
                if nb_path.is_absolute():
                    pass
                elif (repo_root / f).exists():
                    nb_path = repo_root / f
                elif nb_path.exists():
                    pass
                else:
                    print(f"[ERROR] Notebook not found: {nb_path}", file=sys.stderr)
                    continue
                notebooks.append(str(nb_path))
            if not notebooks:
                print("[ERROR] No valid notebooks specified with --files.", file=sys.stderr)
                sys.exit(1)
        else:
            if not notebooks_yaml.exists():
                print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
                sys.exit(1)
            notebooks = parse_yaml_list(notebooks_yaml)
        for nb in notebooks:
            nb_path = repo_root / nb
            if nb_path.exists():
                process_file_for_images(nb_path, nb_stem=Path(nb).stem)
            md_path = nb_path.with_suffix('.md')
            if md_path.exists():
                process_file_for_images(md_path, nb_stem=Path(nb).stem)
        print(f"[INFO] All referenced images copied to {img_dir}")
        return

    # --- Setup logging ---
    log_dir = repo_root / 'log'
    log_dir.mkdir(parents=True, exist_ok=True)
    build_log = log_dir / 'build.log'
    prior_log = log_dir / 'build.log.prior'
    if build_log.exists():
        shutil.copy2(build_log, prior_log)
    log_file = open(build_log, 'w')
    log_stream = contextlib.ExitStack()
    log_stream.enter_context(contextlib.redirect_stdout(log_file))
    log_stream.enter_context(contextlib.redirect_stderr(log_file))
    # All print() and errors after this point go to build.log

    # Determine what to build
    build_latex = args.latex or (not args.pdf and not args.md and not args.docx)
    build_pdf = args.pdf or (not args.latex and not args.md and not args.docx)
    build_md = args.md or (not args.latex and not args.pdf and not args.docx)
    build_docx = args.docx or (not args.latex and not args.pdf and not args.md)

    # Parse notebook list, or use --files if given
    if args.files:
        notebooks = []
        for f in args.files:
            nb_path = Path(f)
            if nb_path.is_absolute():
                pass
            elif (repo_root / f).exists():
                nb_path = repo_root / f
            elif nb_path.exists():
                pass
            else:
                print(f"[ERROR] Notebook not found: {nb_path}", file=sys.stderr)
                continue
            notebooks.append(str(nb_path))
        if not notebooks:
            print("[ERROR] No valid notebooks specified with --files.", file=sys.stderr)
            sys.exit(1)
        image_collection_mode = 'per-notebook'
    else:
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)
        image_collection_mode = 'global'

    # --- Efficient global image collection for full build ---
    if image_collection_mode == 'global':
        img_dir = build_dir / 'images'
        img_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] [Full Build] Collecting all images for all notebooks into {img_dir}")
        def process_file_for_images(file_path, nb_stem=None):
            from fetch_youtube import fetch_youtube_thumbnail
            if not file_path.exists():
                print(f"[WARN] File not found: {file_path}")
                return
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            img_links = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
            img_links += re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', content)
            for img_path in set(img_links):
                yt_match = re.match(r'https?://img\.youtube\.com/vi/([\w-]{11})/', img_path)
                if yt_match:
                    video_id = yt_match.group(1)
                    flat_name = f"{nb_stem}_youtube_{video_id}.jpg" if nb_stem else f"youtube_{video_id}.jpg"
                    dst_img = img_dir / flat_name
                    if fetch_youtube_thumbnail(video_id, dst_img):
                        print(f"[IMG] Downloaded YouTube thumbnail for {video_id} to {dst_img}")
                    else:
                        print(f"[WARN] Could not fetch YouTube thumbnail for {video_id}")
                    continue
                if img_path.startswith('http'):
                    img_filename = os.path.basename(img_path.split('?')[0])
                    flat_name = f"{nb_stem}_{img_filename}" if nb_stem else img_filename
                    dst_img = img_dir / flat_name
                    try:
                        resp = requests.get(img_path, timeout=15)
                        if resp.status_code == 200:
                            with open(dst_img, 'wb') as outimg:
                                outimg.write(resp.content)
                            print(f"[IMG] Downloaded remote image {img_path} to {dst_img}")
                        else:
                            print(f"[WARN] Failed to download image {img_path}: HTTP {resp.status_code}")
                    except Exception as e:
                        print(f"[WARN] Could not download image {img_path}: {e}")
                    continue
                found = False
                real_img_path = None
                img_filename = os.path.basename(img_path)
                if not os.path.isabs(img_path) and not img_path.startswith('~'):
                    candidate = (file_path.parent / img_path).resolve()
                    if candidate.exists():
                        real_img_path = candidate
                        found = True
                if not found:
                    for images_root in images_root_candidates:
                        norm_img_path = os.path.normpath(img_path).lstrip(os.sep)
                        candidate = images_root / norm_img_path
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                if not found:
                    for images_root in images_root_candidates:
                        candidate = images_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                for fallback_root in [repo_root / 'content/notebooks/_images', repo_root / '_images']:
                    if not found:
                        candidate = fallback_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                if not found:
                    html_img_root = repo_root / '_build/html/images'
                    candidate = html_img_root / img_filename
                    if candidate.exists():
                        real_img_path = candidate
                        found = True
                    if not found:
                        for subdir, _, files in os.walk(html_img_root):
                            if img_filename in files:
                                real_img_path = Path(subdir) / img_filename
                                found = True
                                break
                if not found and os.path.dirname(img_path):
                    norm_img_path = os.path.normpath(img_path).lstrip(os.sep)
                    for images_root in images_root_candidates:
                        for subdir, _, files in os.walk(images_root):
                            candidate = Path(subdir) / Path(norm_img_path)
                            if candidate.exists():
                                real_img_path = candidate
                                found = True
                                break
                        if found:
                            break
                if not found:
                    for images_root in images_root_candidates:
                        for subdir, _, files in os.walk(images_root):
                            if img_filename in files:
                                real_img_path = Path(subdir) / img_filename
                                found = True
                                break
                        if found:
                            break
                if found and real_img_path:
                    flat_name = f"{nb_stem}_{img_filename}" if nb_stem else img_filename
                    dst_img = img_dir / flat_name
                    try:
                        shutil.copy2(real_img_path, dst_img)
                        print(f"[IMG] Copied {img_path} from {real_img_path} to {dst_img}")
                    except Exception as e:
                        print(f"[WARN] Could not copy image {real_img_path} to {dst_img}: {e}")
                else:
                    print(f"[WARN] Could not find image: {img_path}")
        for nb in notebooks:
            nb_path = repo_root / nb
            if nb_path.exists():
                process_file_for_images(nb_path, nb_stem=Path(nb).stem)
            md_path = nb_path.with_suffix('.md')
            if md_path.exists():
                process_file_for_images(md_path, nb_stem=Path(nb).stem)
        print(f"[INFO] [Full Build] All referenced images copied to {img_dir}")

    # --- Build TeX ---
    jupyter_bin = str(repo_root / '.venv' / 'bin' / 'jupyter')
    tex_images_dir = chapters_dir / 'images'
    if build_latex:
        chapters_dir.mkdir(parents=True, exist_ok=True)
        tex_images_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Building TeX files for notebooks in project (absolute paths) -> {chapters_dir}")
        for nb in notebooks:
            nb_path = repo_root / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            tex_name = nb_path.with_suffix('.tex').name
            tex_path = chapters_dir / tex_name
            print(f"Converting {nb_path} to {tex_path}")
            missing_images = set()
            try:
                import nbformat
                nb_data = nbformat.read(str(nb_path), as_version=4)
                for cell in nb_data.get('cells', []):
                    if cell.get('cell_type') == 'markdown':
                        cell_source = ''.join(cell.get('source', []))
                        for img_path in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', cell_source):
                            if img_path.startswith('http'):
                                continue
                            img_filename = f"{nb_path.stem}_{os.path.basename(img_path)}"
                            img_file = tex_images_dir / img_filename
                            if not img_file.exists():
                                missing_images.add(img_path)
            except Exception as e:
                print(f"[WARN] Could not parse notebook for images: {e}")
            if missing_images:
                print(f"[INFO] Missing images for {nb_path}: {missing_images}. Running --img...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ], check=True)
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {nb_path}: {e}")
            run_or_exit([
                jupyter_bin, 'nbconvert', '--to', 'latex', str(nb_path),
                '--output', tex_name, '--output-dir', str(chapters_dir)
            ], check=True)
            if tex_path.exists():
                with open(tex_path, 'r', encoding='utf-8') as f:
                    tex_content = f.read()
                def replace_graphics(match):
                    img_path = match.group(2)
                    img_filename = os.path.basename(img_path)
                    if img_filename.startswith(f"{nb_path.stem}_"):
                        flat_name = img_filename
                    else:
                        flat_name = f"{nb_path.stem}_{img_filename}"
                    return f"{match.group(1)}{{../images/{flat_name}}}"
                tex_content = re.sub(r'(\\includegraphics(?:\[[^\]]*\])?)\{([^}]+)\}', replace_graphics, tex_content)
                with open(tex_path, 'w', encoding='utf-8') as f:
                    f.write(tex_content)
        print(f"[INFO] All notebooks converted to TeX and saved in {chapters_dir}. All image links updated to reference _build/images.")

    log_file.close()
    log_stream.close()

    # --- Build PDFs from TeX (compile in place and copy PDFs to {pdf_dir}) ---
    if build_pdf:
        pdf_dir = build_dir / 'pdf'
        pdf_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Compiling TeX files in {chapters_dir} and copying PDFs to {pdf_dir}")
        # Only process tex files corresponding to the notebooks list
        tex_files = []
        for nb in notebooks:
            tex_name = Path(nb).with_suffix('.tex').name
            tex_path = chapters_dir / tex_name
            tex_files.append(tex_path)
        for tex_file in tex_files:
            pdf_name = tex_file.with_suffix('.pdf').name
            pdf_path = chapters_dir / pdf_name
            # Check if .tex file exists, else try to build it with --tex and --files
            if not tex_file.exists():
                print(f"[WARN] .tex file not found: {tex_file}. Attempting to build with --tex...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--latex', '--files', str(tex_file.stem + '.ipynb')
                    ], check=True)
                except Exception as e:
                    print(f"[ERROR] Failed to build TeX for {tex_file}: {e}")
                if not tex_file.exists():
                    print(f"[ERROR] .tex file still not found for {tex_file} after attempting to build. Skipping PDF for this file.")
                    continue
            # Check if all referenced images exist in _build/images, else try to build with --img
            with open(tex_file, 'r', encoding='utf-8') as f:
                tex_content = f.read()
            img_paths = re.findall(r'\\includegraphics(?:\\[[^\\]]*\\])?\\{\\.\\./images/([^}]+)\\}', tex_content)
            missing_images = []
            for img_filename in set(img_paths):
                img_path = repo_root / '_build/images' / img_filename
                if not img_path.exists():
                    missing_images.append(img_filename)
            if missing_images:
                print(f"[WARN] Missing images for {tex_file}: {missing_images}. Attempting to collect with --img...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--img', '--files', str(tex_file.stem + '.ipynb')
                    ], check=True)
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {tex_file}: {e}")
                # Re-check if all images now exist
                still_missing = []
                for img_filename in missing_images:
                    img_path = repo_root / '_build/images' / img_filename
                    if not img_path.exists():
                        still_missing.append(img_filename)
                if still_missing:
                    print(f"[ERROR] Still missing images for {tex_file}: {still_missing}. Skipping PDF for this file.")
                    continue
            print(f"[INFO] Compiling {tex_file} to {pdf_path} using pdflatex...")
            run_or_exit([
                'pdflatex', '-interaction=nonstopmode', str(tex_file)
            ], cwd=chapters_dir, check=True)
            if pdf_path.exists():
                dest_pdf = pdf_dir / pdf_name
                shutil.copy2(pdf_path, dest_pdf)
                print(f"[INFO] Copied {pdf_path} to {dest_pdf}")
            else:
                print(f"[ERROR] PDF not generated for {tex_file}")
        print(f"[INFO] All TeX files compiled and PDFs copied to {pdf_dir}")

    # --- Build Markdown ---
    if build_md:
        md_dir = build_dir / 'md'
        images_dir = build_dir / 'images'  # Use the global images dir
        md_dir.mkdir(parents=True, exist_ok=True)
        images_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Building Markdown files for notebooks in project (absolute paths) -> {md_dir}")
        for nb in notebooks:
            nb_path = repo_root / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            md_name = nb_path.with_suffix('.md').name
            md_path = md_dir / md_name
            print(f"Converting {nb_path} to {md_path}")
            missing_images = set()
            try:
                import nbformat
                nb_data = nbformat.read(str(nb_path), as_version=4)
                for cell in nb_data.get('cells', []):
                    if cell.get('cell_type') == 'markdown':
                        cell_source = ''.join(cell.get('source', []))
                        for img_path in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', cell_source):
                            if img_path.startswith('http'):
                                continue
                            img_filename = f"{nb_path.stem}_{os.path.basename(img_path)}"
                            img_file = images_dir / img_filename
                            if not img_file.exists():
                                missing_images.add(img_path)
            except Exception as e:
                print(f"[WARN] Could not parse notebook for images: {e}")
            if missing_images:
                print(f"[INFO] Missing images for {nb_path}: {missing_images}. Running --img...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {nb_path}: {e}")
            run_or_exit([
                jupyter_bin, 'nbconvert', '--to', 'markdown', str(nb_path),
                '--output', md_name, '--output-dir', str(md_dir)
            ])
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            def replace_img_link(match):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    return match.group(0)  # leave remote images unchanged
                img_filename = os.path.basename(img_path)
                if img_filename.startswith(f"{nb_path.stem}_"):
                    flat_name = img_filename
                else:
                    flat_name = f"{nb_path.stem}_{img_filename}"
                return match.group(0).replace(img_path, f"../images/{flat_name}")
            new_md_content = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', replace_img_link, md_content)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_md_content)
        print(f"[INFO] All notebooks converted to Markdown. All image links updated to reference _build/images.")

    # --- Build DOCX from Markdown ---
    if build_docx:
        md_dir = build_dir / 'md'
        images_dir = build_dir / 'images'  # Use the global images dir, same as Markdown
        docx_dir = build_dir / 'docx'
        docx_dir.mkdir(parents=True, exist_ok=True)
        for nb in notebooks:
            md_name = Path(nb).with_suffix('.md').name
            md_path = md_dir / md_name
            docx_name = Path(nb).with_suffix('.docx').name
            docx_path = docx_dir / docx_name
            # If markdown does not exist, try to build it once, then try again
            if not md_path.exists():
                print(f"[WARN] Markdown not found: {md_path}. Attempting to build it with --md...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--md', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to build markdown for {nb}: {e}")
                if not md_path.exists():
                    print(f"[ERROR] Markdown still not found for {md_path} after attempting to build. Skipping DOCX for this file.")
                    continue
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            missing_images = set()
            for match in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', md_content):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    continue
                img_filename = os.path.basename(img_path)
                flat_name = f"{Path(nb).stem}_{img_filename}"
                img_file = images_dir / flat_name
                if not img_file.exists():
                    missing_images.add(img_path)
            if missing_images:
                print(f"[INFO] Missing images for DOCX in {md_path}: {missing_images}. Running --img...")
                try:
                    run_or_exit([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for DOCX for {nb}: {e}")
            def replace_img_link_docx(match):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    return match.group(0)
                img_filename = os.path.basename(img_path)
                if img_filename.startswith(f"{Path(nb).stem}_"):
                    flat_name = img_filename
                else:
                    flat_name = f"{Path(nb).stem}_{img_filename}"
                return match.group(0).replace(img_path, f"images/{flat_name}")
            new_md_content = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', replace_img_link_docx, md_content)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_md_content)
            print(f"Converting {md_path} to {docx_path} using pandoc with resource-path {build_dir}")
            run_or_exit([
                'pandoc', str(md_path), '-o', str(docx_path), '--resource-path', str(build_dir)
            ], cwd=md_dir)
        print(f"[INFO] All markdown files converted to DOCX using pandoc and saved in {docx_dir}")

    # --- Generate _toc.yml ---
    toc_yml = repo_root / '_toc.yml'
    print(f"[INFO] Generating _toc.yml from {notebooks_yaml} using Python...")
    index_md = repo_root / 'content/index.md'
    if not index_md.exists():
        print(f"[ERROR] content/index.md not found. This file is required as the root for the Jupyter Book.", file=sys.stderr)
        sys.exit(1)
    toc_content = [
        "# Auto-generated _toc.yml from _notebooks.yaml",
        "format: jb-book",
        "root: content/index",
        "chapters:",
    ]
    for nb in notebooks:
        nb_path = Path(nb)
        # Remove .ipynb suffix for toc, keep path as in _notebooks.yaml
        file_entry = str(nb_path.with_suffix(''))
        # Do not include content/index as a chapter (should only be root)
        if file_entry == "content/index":
            continue
        toc_content.append(f"  - file: {file_entry}")
    with open(toc_yml, 'w') as f:
        f.write('\n'.join(toc_content) + '\n')
    print(f"[INFO] _toc.yml generated with {len([nb for nb in notebooks if Path(nb).with_suffix('') != 'content/index'])} chapters.")

    # Clean up step removed: Do not remove any folders or files in _build during the build process.
    # If cleanup is needed, it should be a separate explicit step, not part of the main build.

if __name__ == '__main__':
    main()
