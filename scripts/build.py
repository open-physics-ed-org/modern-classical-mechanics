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
    parser = argparse.ArgumentParser(description="Build PDFs, Markdown, DOCX, and HTML from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
    parser.add_argument('--md', action='store_true', help='Build Markdown only')
    parser.add_argument('--docx', action='store_true', help='Build DOCX only')
    parser.add_argument('--html', action='store_true', help='Build HTML only')
    args = parser.parse_args()

    # Directories
    current_dir = Path(__file__).parent.resolve()
    repo_root = current_dir.parent
    build_dir = repo_root / '_build'
    chapters_dir = build_dir / 'latex'
    html_dir = build_dir / 'html'
    notebook_dir = repo_root / 'notebooks'
    notebooks_yaml = repo_root / 'notebooks.yaml'
    update_toc = repo_root / 'scripts' / 'update_toc.sh'
    fetch_images = repo_root / 'scripts' / 'fetch_remote_images.sh'

    build_pdf = args.pdf or (not args.md and not args.docx and not args.html)
    build_md = args.md or (not args.pdf and not args.docx and not args.html)
    build_docx = args.docx or (not args.pdf and not args.md and not args.html)
    build_html = args.html or (not args.pdf and not args.md and not args.docx)

    # Always generate _toc.yml from notebooks.yaml using Python (robust, no timestamp logic)
    toc_yml = repo_root / '_toc.yml'
    print(f"[INFO] Generating _toc.yml from {notebooks_yaml} using Python...")
    if not notebooks_yaml.exists():
        print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
        sys.exit(1)
    notebooks = parse_yaml_list(notebooks_yaml)
    toc_content = [
        "# Auto-generated _toc.yml from notebooks.yaml",
        "format: jb-book",
        "root: intro",
        "chapters:",
    ]
    for nb in notebooks:
        nb_path = Path(nb)
        toc_content.append(f"  - file: notebooks/{nb_path.stem}")
    # If intro.md does not exist, use the first notebook as root and the rest as chapters
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

    # Always fetch remote images and update references
    print(f"[INFO] Fetching remote images and updating references...")
    run([str(fetch_images)])
    print(f"[INFO] Remote image fetch and update complete.")

    # Build PDFs, Markdown, and DOCX for each notebook, controlled by CLI flags
    if build_pdf:
        fmt, outdir = 'pdf', 'latex'
        output_dir = build_dir / outdir
        print(f"[INFO] Building chapter {fmt.upper()}s in {output_dir}...")
        output_dir.mkdir(parents=True, exist_ok=True)
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            out_file = output_dir / (nb_path.stem + '.pdf')
            if not out_file.exists() or nb_path.stat().st_mtime > out_file.stat().st_mtime:
                print(f"[INFO] Converting {nb_path} to {out_file}")
                run(['jupyter', 'nbconvert', '--to', fmt, str(nb_path), '--output', out_file.name, '--output-dir', str(output_dir)])
            else:
                print(f"[SKIP] {out_file} is up to date.")
        # Clean up output_dir: remove all files/folders except chapter outputs
        keep_files = {Path(nb).stem + '.pdf' for nb in notebooks}
        for f in output_dir.iterdir():
            if f.is_file() and f.name not in keep_files:
                try:
                    f.unlink()
                    print(f"[INFO] Removed {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove {f}: {e}")
            elif f.is_dir() and f.name not in {'html', 'md', 'docx'}:
                try:
                    shutil.rmtree(f)
                    print(f"[INFO] Removed directory {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove directory {f}: {e}")

    if build_md:
        fmt, outdir = 'markdown', 'md'
        output_dir = build_dir / outdir
        print(f"[INFO] Building chapter {fmt.upper()}s in {output_dir}...")
        output_dir.mkdir(parents=True, exist_ok=True)
        images_dir = output_dir / 'images'
        images_dir.mkdir(parents=True, exist_ok=True)
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)
        import re
        import hashlib
        image_pattern = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
        keep_files = set()
        keep_images = set()
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            out_file = output_dir / (nb_path.stem + '.md')
            if not out_file.exists() or nb_path.stat().st_mtime > out_file.stat().st_mtime:
                print(f"[INFO] Converting {nb_path} to {out_file}")
                run(['jupyter', 'nbconvert', '--to', fmt, str(nb_path), '--output', out_file.name, '--output-dir', str(output_dir)])
            else:
                print(f"[SKIP] {out_file} is up to date.")
            # Now process the markdown for images
            if out_file.exists():
                with open(out_file, 'r', encoding='utf-8') as f:
                    md = f.read()
                def replace_image(match):
                    img_path = match.group(1)
                    # Only handle local images (not http/https)
                    if img_path.startswith('http://') or img_path.startswith('https://'):
                        return match.group(0)
                    # Flatten the image name using a hash to avoid collisions
                    img_name = os.path.basename(img_path)
                    # Add hash of original path for uniqueness
                    hash_digest = hashlib.md5(img_path.encode('utf-8')).hexdigest()[:8]
                    flat_name = f"{hash_digest}_{img_name}"
                    src_img = (nb_path.parent / img_path).resolve()
                    dest_img = images_dir / flat_name
                    if src_img.exists():
                        shutil.copy2(src_img, dest_img)
                        keep_images.add(flat_name)
                        return match.group(0).replace(img_path, f'images/{flat_name}')
                    else:
                        print(f"[WARN] Image not found: {src_img}")
                        return match.group(0)
                new_md = image_pattern.sub(replace_image, md)
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(new_md)
            keep_files.add(out_file.name)
        # Clean up output_dir: remove all files/folders except chapter outputs and images dir
        for f in output_dir.iterdir():
            if f.is_file() and f.name not in keep_files:
                try:
                    f.unlink()
                    print(f"[INFO] Removed {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove {f}: {e}")
            elif f.is_dir() and f.name != 'images' and f.name not in {'html', 'md', 'docx'}:
                try:
                    shutil.rmtree(f)
                    print(f"[INFO] Removed directory {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove directory {f}: {e}")
        # Clean up images_dir: remove images not referenced
        for img in images_dir.iterdir():
            if img.is_file() and img.name not in keep_images:
                try:
                    img.unlink()
                    print(f"[INFO] Removed unused image {img}")
                except Exception as e:
                    print(f"[WARN] Could not remove image {img}: {e}")

    if build_docx:
        fmt, outdir = 'docx', 'docx'
        output_dir = build_dir / outdir
        print(f"[INFO] Building chapter {fmt.upper()}s in {output_dir}...")
        output_dir.mkdir(parents=True, exist_ok=True)
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            out_file = output_dir / (nb_path.stem + '.docx')
            if not out_file.exists() or nb_path.stat().st_mtime > out_file.stat().st_mtime:
                print(f"[INFO] Converting {nb_path} to {out_file}")
                run(['jupyter', 'nbconvert', '--to', fmt, str(nb_path), '--output', out_file.name, '--output-dir', str(output_dir)])
            else:
                print(f"[SKIP] {out_file} is up to date.")
        keep_files = {Path(nb).stem + '.docx' for nb in notebooks}
        for f in output_dir.iterdir():
            if f.is_file() and f.name not in keep_files:
                try:
                    f.unlink()
                    print(f"[INFO] Removed {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove {f}: {e}")
            elif f.is_dir() and f.name not in {'html', 'md', 'docx'}:
                try:
                    shutil.rmtree(f)
                    print(f"[INFO] Removed directory {f}")
                except Exception as e:
                    print(f"[WARN] Could not remove directory {f}: {e}")
    # Remove all folders in _build except latex, html, md, docx
    for f in build_dir.iterdir():
        if f.is_dir() and f.name not in {'latex', 'html', 'md', 'docx'}:
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

    # Build HTML
    if build_html:
        print(f"[INFO] Building Jupyter Book HTML in {html_dir}...")
        run(['jupyter-book', 'build', str(repo_root), '--path-output', str(build_dir), '--builder', 'html'])
        if html_dir.exists():
            print(f"[INFO] Jupyter Book HTML build complete. Output in {html_dir}")
        else:
            print(f"[WARN] HTML output directory not found: {html_dir}")

    print(f"[INFO] Build process finished. Output directory: {build_dir}")

if __name__ == '__main__':
    main()
