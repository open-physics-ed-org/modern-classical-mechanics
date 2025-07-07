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

def run(cmd, **kwargs):
    print(f"[RUN] {' '.join(str(x) for x in cmd)}")
    result = subprocess.run(cmd, **kwargs)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {' '.join(str(x) for x in cmd)}", file=sys.stderr)
        sys.exit(result.returncode)

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
    parser = argparse.ArgumentParser(description="Build PDFs, Markdown, DOCX, HTML, or just collect all images from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
    parser.add_argument('--md', action='store_true', help='Build Markdown only')
    parser.add_argument('--docx', action='store_true', help='Build DOCX only')
    parser.add_argument('--latex', action='store_true', help='Build TeX only')
    parser.add_argument('--html', action='store_true', help='Build HTML only')
    parser.add_argument('--img', action='store_true', help='Collect all referenced images into _build/images/')
    parser.add_argument('--files', nargs='+', help='One or more notebook files to build (relative to notebooks/ or absolute)')
    args = parser.parse_args()

    # Directories and image search roots (must be set before any logic or function that uses them)
    repo_root = Path(__file__).parent.resolve()
    build_dir = repo_root / '_build'
    build_dir.mkdir(parents=True, exist_ok=True)  # Ensure _build exists
    chapters_dir = build_dir / 'tex'
    html_dir = build_dir / 'html'
    notebook_dir = repo_root / 'content/notebooks'
    # Use _notebooks.yaml instead of notebooks.yaml
    notebooks_yaml = repo_root / '_notebooks.yaml'
    update_toc = repo_root / 'scripts' / 'update_toc.sh'
    images_root_candidates = [repo_root / 'images', repo_root / 'content/images']

    # --- Build Images Only ---
    if hasattr(args, 'img') and args.img:
        img_dir = build_dir / 'images'
        img_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Collecting all images referenced in notebooks and markdown into {img_dir}")
        # Helper to process a file and copy all images it references
        def process_file_for_images(file_path, nb_stem=None):
            import re
            import requests
            from fetch_youtube import fetch_youtube_thumbnail
            if not file_path.exists():
                print(f"[WARN] File not found: {file_path}")
                return
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Markdown image links: ![...](...)
            img_links = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
            # LaTeX image links: \includegraphics{...}
            img_links += re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', content)
            for img_path in set(img_links):
                # --- YouTube thumbnail handling ---
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
                    # Download remote image (non-YouTube)
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
                # --- Local/relative image handling ---
                found = False
                real_img_path = None
                img_filename = os.path.basename(img_path)
                # 1. Try resolving the full relative path from the file's location
                if not os.path.isabs(img_path) and not img_path.startswith('~'):
                    # If file_path is a notebook or markdown, resolve relative to its parent
                    candidate = (file_path.parent / img_path).resolve()
                    if candidate.exists():
                        real_img_path = candidate
                        found = True
                # 2. Try to find the full subpath in each images_root_candidates
                if not found:
                    for images_root in images_root_candidates:
                        # Remove any leading ../ or ./ from img_path for subpath search
                        norm_img_path = os.path.normpath(img_path).lstrip(os.sep)
                        candidate = images_root / norm_img_path
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                # 3. Try by filename in images_root_candidates (legacy logic)
                if not found:
                    for images_root in images_root_candidates:
                        candidate = images_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                # 4. Try notebook_dir/_images, repo_root/_images
                if not found:
                    for fallback_root in [notebook_dir / '_images', repo_root / '_images']:
                        candidate = fallback_root / img_filename
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                # 5. Try _build/html/images and all subfolders recursively
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
                # 6. As a last resort, search recursively in all images_root_candidates for the full subpath (if any subdirs in img_path)
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
                # 7. As a final fallback, search recursively for the filename only (legacy logic)
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
        # Process all notebooks and markdown files in content/notebooks
        # Need to parse notebook list before this block
        if args.files:
            notebooks = []
            for f in args.files:
                nb_path = Path(f)
                if nb_path.is_absolute():
                    pass
                elif (notebook_dir / nb_path).exists():
                    nb_path = notebook_dir / nb_path
                elif nb_path.exists():
                    pass
                else:
                    print(f"[ERROR] Notebook not found: {nb_path}", file=sys.stderr)
                    continue
                try:
                    rel = nb_path.relative_to(notebook_dir)
                    notebooks.append(str(rel))
                except ValueError:
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
            nb_path = notebook_dir / nb
            if nb_path.exists():
                process_file_for_images(nb_path, nb_stem=nb_path.stem)
            # Also process corresponding markdown if it exists
            md_path = nb_path.with_suffix('.md')
            if md_path.exists():
                process_file_for_images(md_path, nb_stem=nb_path.stem)
        print(f"[INFO] All referenced images copied to {img_dir}")
        return

    # Directories (must be set before logging)
    repo_root = Path(__file__).parent.resolve()
    build_dir = repo_root / '_build'
    build_dir.mkdir(parents=True, exist_ok=True)  # Ensure _build exists
    chapters_dir = build_dir / 'latex'
    html_dir = build_dir / 'html'
    notebook_dir = repo_root / 'content/notebooks'
    # Use _notebooks.yaml instead of notebooks.yaml
    notebooks_yaml = repo_root / '_notebooks.yaml'
    update_toc = repo_root / 'scripts' / 'update_toc.sh'

    # --- Setup logging ---
    log_dir = repo_root / 'log'
    log_dir.mkdir(parents=True, exist_ok=True)
    build_log = log_dir / 'build.log'
    prior_log = log_dir / 'build.log.prior'
    if build_log.exists():
        shutil.copy2(build_log, prior_log)
    import contextlib
    log_file = open(build_log, 'w')
    log_stream = contextlib.ExitStack()
    log_stream.enter_context(contextlib.redirect_stdout(log_file))
    log_stream.enter_context(contextlib.redirect_stderr(log_file))
    # All print() and errors after this point go to build.log

    parser = argparse.ArgumentParser(description="Build PDFs, Markdown, DOCX, HTML, or just collect all images from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
    parser.add_argument('--md', action='store_true', help='Build Markdown only')
    parser.add_argument('--docx', action='store_true', help='Build DOCX only')
    parser.add_argument('--latex', action='store_true', help='Build LaTeX only')
    parser.add_argument('--html', action='store_true', help='Build HTML only')
    parser.add_argument('--img', action='store_true', help='Collect all referenced images into _build/images/')
    parser.add_argument('--files', nargs='+', help='One or more notebook files to build (relative to notebooks/ or absolute)')
    args = parser.parse_args()

    import nbformat
    import requests
    import re
    import hashlib

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
            # If already absolute, use as is
            if nb_path.is_absolute():
                pass
            # If already relative to notebook_dir, use as is
            elif (notebook_dir / nb_path).exists():
                nb_path = notebook_dir / nb_path
            # If relative to cwd and exists, use as is
            elif nb_path.exists():
                pass
            else:
                print(f"[ERROR] Notebook not found: {nb_path}", file=sys.stderr)
                continue
            # Store as relative to notebook_dir if possible
            try:
                rel = nb_path.relative_to(notebook_dir)
                notebooks.append(str(rel))
            except ValueError:
                notebooks.append(str(nb_path))
        if not notebooks:
            print("[ERROR] No valid notebooks specified with --files.", file=sys.stderr)
            sys.exit(1)
    else:
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)

    # --- Build TeX ---
    jupyter_bin = str(repo_root / '.venv' / 'bin' / 'jupyter')
    images_root_candidates = [repo_root / 'images', repo_root / 'content/images']
    tex_images_dir = chapters_dir / 'images'
    if args.latex or (not args.pdf and not args.md and not args.docx):
        chapters_dir.mkdir(parents=True, exist_ok=True)
        tex_images_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Building TeX files for notebooks in {notebook_dir} -> {chapters_dir}")
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            tex_name = nb_path.with_suffix('.tex').name
            tex_path = chapters_dir / tex_name
            print(f"Converting {nb_path} to {tex_path}")
            # Before conversion, check for missing images referenced in the notebook and fetch them if needed
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
                    run([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {nb_path}: {e}")
            # Now convert to TeX
            run([
                jupyter_bin, 'nbconvert', '--to', 'latex', str(nb_path),
                '--output', tex_name, '--output-dir', str(chapters_dir)
            ])
            # Update image links in the .tex file to use ../images/{flat_name}
            if tex_path.exists():
                with open(tex_path, 'r', encoding='utf-8') as f:
                    tex_content = f.read()
                def replace_graphics(match):
                    img_path = match.group(2)
                    img_filename = os.path.basename(img_path)
                    # Only prepend nb_path.stem if not already present
                    if img_filename.startswith(f"{nb_path.stem}_"):
                        flat_name = img_filename
                    else:
                        flat_name = f"{nb_path.stem}_{img_filename}"
                    return f"{match.group(1)}{{../images/{flat_name}}}"
                # Replace all \includegraphics{...} with correct flat_name
                tex_content = re.sub(r'(\\includegraphics(?:\[[^\]]*\])?)\{([^}]+)\}', replace_graphics, tex_content)
                with open(tex_path, 'w', encoding='utf-8') as f:
                    f.write(tex_content)
        print(f"[INFO] All notebooks converted to TeX and saved in {chapters_dir}. All image links updated to reference _build/images.")

    # --- End logging ---
    log_file.close()
    log_stream.close()

    # --- Build PDFs from TeX (compile in place and copy PDFs) ---
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
                    run([
                        sys.executable, __file__, '--tex', '--files', str(tex_file.stem + '.ipynb')
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to build TeX for {tex_file}: {e}")
                if not tex_file.exists():
                    print(f"[ERROR] .tex file still not found for {tex_file} after attempting to build. Skipping PDF for this file.")
                    continue
            # Check if all referenced images exist in _build/images, else try to build with --img
            with open(tex_file, 'r', encoding='utf-8') as f:
                tex_content = f.read()
            img_paths = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{\.\./images/([^}]+)\}', tex_content)
            missing_images = []
            for img_filename in set(img_paths):
                img_path = repo_root / '_build/images' / img_filename
                if not img_path.exists():
                    missing_images.append(img_filename)
            if missing_images:
                print(f"[WARN] Missing images for {tex_file}: {missing_images}. Attempting to collect with --img...")
                try:
                    run([
                        sys.executable, __file__, '--img', '--files', str(tex_file.stem + '.ipynb')
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {tex_file}: {e}")
                # Re-check if all images now exist
                still_missing = []
                for img_filename in missing_images:
                    img_path = repo_root / '_build/images' / img_filename
                    if not img_path.exists():
                        still_missing.append(img_filename)
                if still_missing:
                    print(f"[ERROR] Images still missing for {tex_file}: {still_missing}. Skipping PDF for this file.")
                    continue
            print(f"[INFO] Compiling {tex_file} to {pdf_path} using pdflatex...")
            run([
                'pdflatex', '-interaction=nonstopmode', str(tex_file)
            ], cwd=chapters_dir)
            if pdf_path.exists():
                dest_pdf = pdf_dir / pdf_name
                shutil.copy2(pdf_path, dest_pdf)
                print(f"[INFO] Copied {pdf_path} to {dest_pdf}")
            else:
                print(f"[ERROR] PDF not generated for {tex_file}", file=sys.stderr)
        print(f"[INFO] All TeX files compiled and PDFs copied to {pdf_dir}")

    # --- Build Markdown ---
    if build_md:
        md_dir = build_dir / 'md'
        images_dir = build_dir / 'images'  # Use the global images dir
        md_dir.mkdir(parents=True, exist_ok=True)
        images_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Building Markdown files for notebooks in {notebook_dir} -> {md_dir}")
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            md_name = nb_path.with_suffix('.md').name
            md_path = md_dir / md_name
            print(f"Converting {nb_path} to {md_path}")
            # Before conversion, check for missing images referenced in the notebook and fetch them if needed
            # 1. Parse notebook for image links
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
            # 2. If any missing images, run --img for this notebook
            if missing_images:
                print(f"[INFO] Missing images for {nb_path}: {missing_images}. Running --img...")
                try:
                    run([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for {nb_path}: {e}")
            # 3. Now convert to markdown
            run([
                jupyter_bin, 'nbconvert', '--to', 'markdown', str(nb_path),
                '--output', md_name, '--output-dir', str(md_dir)
            ])
            # 4. Update image links in the markdown to point to the global images dir (do not copy images)
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            def replace_img_link(match):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    return match.group(0)  # leave remote images unchanged
                img_filename = os.path.basename(img_path)
                # Only prepend nb_path.stem if not already present
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
                    run([
                        sys.executable, __file__, '--md', '--files', str(nb_path if 'nb_path' in locals() else (notebook_dir / nb))
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to build markdown for {nb}: {e}")
                if not md_path.exists():
                    print(f"[ERROR] Markdown still not found for {md_path} after attempting to build. Skipping DOCX for this file.")
                    continue
            # Ensure all images referenced in the markdown exist in _build/images (same as Markdown logic)
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
                    run([
                        sys.executable, __file__, '--img', '--files', str(nb)
                    ])
                except Exception as e:
                    print(f"[ERROR] Failed to collect images for DOCX for {nb}: {e}")
            # Update image links in the markdown to point to the global images dir (for DOCX: use images/ not ../images/)
            def replace_img_link_docx(match):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    return match.group(0)
                img_filename = os.path.basename(img_path)
                # Only prepend nb stem if not already present
                if img_filename.startswith(f"{Path(nb).stem}_"):
                    flat_name = img_filename
                else:
                    flat_name = f"{Path(nb).stem}_{img_filename}"
                # For DOCX, use images/flat_name (not ../images/)
                return match.group(0).replace(img_path, f"images/{flat_name}")
            new_md_content = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', replace_img_link_docx, md_content)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_md_content)
            print(f"Converting {md_path} to {docx_path} using pandoc with resource-path {build_dir}")
            run([
                'pandoc', str(md_path), '-o', str(docx_path), '--resource-path', str(build_dir)
            ], cwd=md_dir)
        print(f"[INFO] All markdown files converted to DOCX using pandoc and saved in {docx_dir}")

    # --- Generate _toc.yml ---
    toc_yml = repo_root / '_toc.yml'
    print(f"[INFO] Generating _toc.yml from {notebooks_yaml} using Python...")
    toc_content = [
        "# Auto-generated _toc.yml from notebooks.yaml",
        "format: jb-book",
        "root: intro",
        "chapters:",
    ]
    for nb in notebooks:
        nb_path = Path(nb)
        toc_content.append(f"  - file: notebooks/{nb_path.stem}")
    intro_md = repo_root / 'intro.md'
    if not intro_md.exists() and notebooks:
        toc_content = [
            "# Auto-generated _toc.yml from notebooks.yaml",
            "format: jb-book",
            f"root: notebooks/{Path(notebooks[0]).stem}",
            "chapters:",
        ]
        for nb in notebooks[1:]:
            nb_path = Path(nb)
            toc_content.append(f"  - file: notebooks/{nb_path.stem}")
    with open(toc_yml, 'w') as f:
        f.write('\n'.join(toc_content) + '\n')
    print(f"[INFO] _toc.yml generated with {len(notebooks)} chapters.")

    # Clean up: Remove all folders in _build except latex, html, md, docx, pdf
    # Also preserve 'images' directory for Markdown and other builds
    for f in build_dir.iterdir():
        if f.is_dir() and f.name not in {'latex', 'html', 'md', 'docx', 'pdf', 'images'}:
            try:
                shutil.rmtree(f)
                print(f"[INFO] Removed directory {f}")
            except Exception as e:
                print(f"[WARN] Could not remove directory {f}: {e}")
        elif f.is_file():
            try:
                f.unlink()
                print(f"[INFO] Removed {f}")
            except Exception as e:
                print(f"[WARN] Could not remove {f}: {e}")

if __name__ == '__main__':
    main()
