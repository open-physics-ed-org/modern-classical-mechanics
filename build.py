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

    # Directories (must be set before logging)
    repo_root = Path(__file__).parent.resolve()
    build_dir = repo_root / '_build'
    build_dir.mkdir(parents=True, exist_ok=True)  # Ensure _build exists
    chapters_dir = build_dir / 'latex'
    html_dir = build_dir / 'html'
    notebook_dir = repo_root / 'notebooks'
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

    parser = argparse.ArgumentParser(description="Build PDFs, Markdown, DOCX, and HTML from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
    parser.add_argument('--md', action='store_true', help='Build Markdown only')
    parser.add_argument('--docx', action='store_true', help='Build DOCX only')
    parser.add_argument('--latex', action='store_true', help='Build LaTeX only')
    parser.add_argument('--html', action='store_true', help='Build HTML only')
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

    # --- Build LaTeX ---
    jupyter_bin = str(repo_root / '.venv' / 'bin' / 'jupyter')
    if build_latex:
        chapters_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Building LaTeX files for notebooks in {notebook_dir} -> {chapters_dir}")
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            tex_name = nb_path.with_suffix('.tex').name
            tex_path = chapters_dir / tex_name
            print(f"Converting {nb_path} to {tex_path}")
            run([
                jupyter_bin, 'nbconvert', '--to', 'latex', str(nb_path),
                '--output', tex_name, '--output-dir', str(chapters_dir)
            ])
        print(f"[INFO] All notebooks converted to LaTeX and saved in {chapters_dir}")

    # --- End logging ---
    log_file.close()
    log_stream.close()

    # --- Build PDFs from LaTeX (compile in place and copy PDFs) ---
    if build_pdf:
        pdf_dir = build_dir / 'pdf'
        pdf_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Compiling LaTeX files in {chapters_dir} and copying PDFs to {pdf_dir}")
        for tex_file in chapters_dir.glob('*.tex'):
            pdf_name = tex_file.with_suffix('.pdf').name
            pdf_path = chapters_dir / pdf_name
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
        print(f"[INFO] All LaTeX files compiled and PDFs copied to {pdf_dir}")

    # --- Build Markdown ---
    if build_md:
        md_dir = build_dir / 'md'
        images_dir = md_dir / 'images'
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
            run([
                jupyter_bin, 'nbconvert', '--to', 'markdown', str(nb_path),
                '--output', md_name, '--output-dir', str(md_dir)
            ])
            # Copy local images referenced in the markdown to the images directory and update links
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            def replace_img_link(match):
                img_path = match.group(1)
                if img_path.startswith('http'):
                    return match.group(0)  # leave remote images unchanged
                src_img = (nb_path.parent / img_path).resolve()
                if not src_img.exists():
                    alt_img = md_dir / f"{nb_path.stem}_files" / os.path.basename(img_path)
                    if alt_img.exists():
                        src_img = alt_img
                    else:
                        print(f"[WARN] Image not found: {src_img}")
                        return match.group(0)
                flat_name = f"{nb_path.stem}_{os.path.basename(img_path)}"
                dst_img = images_dir / flat_name
                try:
                    shutil.copy2(src_img, dst_img)
                except Exception as e:
                    print(f"[WARN] Could not copy image {src_img} to {dst_img}: {e}")
                # Update the link to point to images/flat_name
                return match.group(0).replace(img_path, f"images/{flat_name}")
            # Replace all image links in the markdown
            new_md_content = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', replace_img_link, md_content)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_md_content)
        print(f"[INFO] All notebooks converted to Markdown. Local images copied to {images_dir}. All image links updated.")

    # --- Build DOCX from Markdown ---
    if build_docx:
        md_dir = build_dir / 'md'
        images_dir = md_dir / 'images'
        docx_dir = build_dir / 'docx'
        docx_dir.mkdir(parents=True, exist_ok=True)
        for nb in notebooks:
            md_name = Path(nb).with_suffix('.md').name
            md_path = md_dir / md_name
            docx_name = Path(nb).with_suffix('.docx').name
            docx_path = docx_dir / docx_name
            if not md_path.exists():
                print(f"[WARN] Markdown not found: {md_path}")
                continue
            print(f"Converting {md_path} to {docx_path} using pandoc with resource-path {md_dir}:{images_dir}")
            run([
                'pandoc', str(md_path), '-o', str(docx_path), '--resource-path', f"{md_dir}:{images_dir}"
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
    for f in build_dir.iterdir():
        if f.is_dir() and f.name not in {'latex', 'html', 'md', 'docx', 'pdf'}:
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
