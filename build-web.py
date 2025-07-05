#!/usr/bin/env python3
"""
build-web.py - Convert all Jupyter notebooks in notebooks/ to HTML and copy to docs/ for static website hosting (e.g., GitHub Pages).
"""
import os
import shutil
from pathlib import Path
import subprocess

def run(cmd):
    print(f"[RUN] {' '.join(str(x) for x in cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(str(x) for x in cmd)}")

def main():
    repo_root = Path(__file__).parent.resolve()
    notebooks_dir = repo_root / 'notebooks'
    docs_dir = repo_root / 'docs'
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Ensure .nojekyll for GitHub Pages
    nojekyll = docs_dir / '.nojekyll'
    if not nojekyll.exists():
        print("Creating docs/.nojekyll to disable Jekyll processing on GitHub Pages")
        nojekyll.touch()

    # Convert all notebooks to HTML and copy to docs/
    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        html_path = docs_dir / html_name
        print(f"Converting {nb} to {html_path}")
        run(['jupyter', 'nbconvert', '--to', 'html', str(nb), '--output', html_name, '--output-dir', str(docs_dir)])

    print("All notebooks converted to HTML and copied to docs/.")
    print("You can now deploy docs/ as a static website (e.g., with GitHub Pages).")

if __name__ == '__main__':
    main()
