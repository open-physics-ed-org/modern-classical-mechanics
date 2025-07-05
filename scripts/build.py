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
    parser = argparse.ArgumentParser(description="Build PDFs and HTML from Jupyter notebooks and Jupyter Book.")
    parser.add_argument('--pdf', action='store_true', help='Build PDFs only')
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

    build_pdf = args.pdf or not args.html
    build_html = args.html or not args.pdf

    # Always update _toc.yml
    print(f"[INFO] Syncing _toc.yml from {notebooks_yaml}...")
    run([str(update_toc)])

    # Always fetch remote images and update references
    print(f"[INFO] Fetching remote images and updating references...")
    run([str(fetch_images)])
    print(f"[INFO] Remote image fetch and update complete.")

    # Build PDFs
    if build_pdf:
        print(f"[INFO] Building chapter PDFs in {chapters_dir}...")
        chapters_dir.mkdir(parents=True, exist_ok=True)
        if not notebooks_yaml.exists():
            print(f"[ERROR] {notebooks_yaml} not found.", file=sys.stderr)
            sys.exit(1)
        notebooks = parse_yaml_list(notebooks_yaml)
        for nb in notebooks:
            nb_path = notebook_dir / nb
            if not nb_path.exists():
                print(f"[WARN] Notebook not found: {nb_path}")
                continue
            pdf_path = chapters_dir / (nb_path.stem + '.pdf')
            if not pdf_path.exists() or nb_path.stat().st_mtime > pdf_path.stat().st_mtime:
                print(f"[INFO] Converting {nb_path} to {pdf_path}")
                run(['jupyter', 'nbconvert', '--to', 'pdf', str(nb_path), '--output', pdf_path.name, '--output-dir', str(chapters_dir)])
            else:
                print(f"[SKIP] {pdf_path} is up to date.")
        # Build full book PDF
        config_yml = repo_root / '_config.yml'
        toc_yml = repo_root / '_toc.yml'
        if config_yml.exists() and toc_yml.exists():
            print(f"[INFO] Building full book PDF with Jupyter Book...")
            # Use repo_root as path-output to avoid nested _build/_build
            run(['jupyter-book', 'build', str(repo_root), '--path-output', str(repo_root), '--builder', 'pdflatex'])
            # Find the generated book PDF (named after the project directory)
            project_pdf = chapters_dir / (repo_root.name + '.pdf')
            final_pdf = chapters_dir / 'book.pdf'
            book_pdf_found = False
            if project_pdf.exists():
                print(f"[INFO] Full book PDF found at {project_pdf}")
                # Optionally copy/rename to book.pdf for consistency
                try:
                    shutil.copy(project_pdf, final_pdf)
                    print(f"[INFO] Copied {project_pdf} to {final_pdf}")
                    book_pdf_found = True
                except Exception as e:
                    print(f"[WARN] Could not copy {project_pdf} to {final_pdf}: {e}")
            else:
                # Fallback: look for any PDF in chapters_dir not matching chapter PDFs
                pdf_candidates = list(chapters_dir.glob('*.pdf'))
                chapter_pdfs = {Path(nb).stem + '.pdf' for nb in notebooks}
                book_pdfs = [p for p in pdf_candidates if p.name not in chapter_pdfs]
                if book_pdfs:
                    print(f"[INFO] Full book PDF found at {book_pdfs[0]}")
                    try:
                        shutil.copy(book_pdfs[0], final_pdf)
                        print(f"[INFO] Copied {book_pdfs[0]} to {final_pdf}")
                        book_pdf_found = True
                    except Exception as e:
                        print(f"[WARN] Could not copy {book_pdfs[0]} to {final_pdf}: {e}")
                else:
                    print(f"[WARN] Full book PDF was not generated in {chapters_dir}")

            # Remove all files and _sphinx_design_static folder in chapters_dir except chapter PDFs and book.pdf
            keep_files = {final_pdf.name} | {Path(nb).stem + '.pdf' for nb in notebooks}
            for f in chapters_dir.iterdir():
                if f.is_file() and f.name not in keep_files:
                    try:
                        f.unlink()
                        print(f"[INFO] Removed {f}")
                    except Exception as e:
                        print(f"[WARN] Could not remove {f}: {e}")
                elif f.is_dir() and f.name.startswith('_sphinx'):
                    try:
                        shutil.rmtree(f)
                        print(f"[INFO] Removed directory {f}")
                    except Exception as e:
                        print(f"[WARN] Could not remove directory {f}: {e}")
        else:
            print(f"[WARN] _config.yml and/or _toc.yml not found. Skipping full book PDF build.")

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
