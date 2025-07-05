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

    # Step 1: Fetch all remote images and update notebook references (like build.py)
    import nbformat
    import requests
    import re
    import hashlib

    for nb_path in notebooks_dir.glob('*.ipynb'):
        try:
            nb_data = nbformat.read(str(nb_path), as_version=4)
        except Exception as e:
            print(f"[WARN] Could not read notebook {nb_path}: {e}")
            continue
        changed = False
        remote_image_pattern = re.compile(r'!\[[^\]]*\]\((https?://[^)]+)\)')
        for cell in nb_data.cells:
            if cell.cell_type != 'markdown':
                continue
            def repl(match):
                url = match.group(1)
                hash_digest = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
                ext = os.path.splitext(url.split('?')[0])[1] or '.img'
                local_name = f"remote_{hash_digest}{ext}"
                local_path = nb_path.parent / local_name
                if not local_path.exists():
                    try:
                        resp = requests.get(url, timeout=10)
                        resp.raise_for_status()
                        with open(local_path, 'wb') as f:
                            f.write(resp.content)
                        print(f"[INFO] Downloaded {url} -> {local_path}")
                    except Exception as e:
                        print(f"[WARN] Failed to fetch {url}: {e}")
                        return match.group(0)
                else:
                    print(f"[INFO] Already downloaded {url} -> {local_path}")
                changed_local = match.group(0).replace(url, local_name)
                return changed_local
            new_src = remote_image_pattern.sub(repl, cell.source)
            if new_src != cell.source:
                cell.source = new_src
                changed = True
        if changed:
            try:
                nbformat.write(nb_data, str(nb_path))
                print(f"[INFO] Updated notebook with local images: {nb_path}")
            except Exception as e:
                print(f"[WARN] Could not write notebook {nb_path}: {e}")

    # Step 2: Copy all images referenced in notebooks to docs/images/ and update references
    images_dir = docs_dir / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)
    for nb_path in notebooks_dir.glob('*.ipynb'):
        nb_data = nbformat.read(str(nb_path), as_version=4)
        changed = False
        for cell in nb_data.cells:
            if cell.cell_type != 'markdown':
                continue
            def copy_and_update(match):
                img_path = match.group(2)
                if img_path.startswith('http'):
                    return match.group(0)
                src_img = (nb_path.parent / img_path).resolve()
                if not src_img.exists():
                    print(f"[WARN] Image not found: {src_img}")
                    return match.group(0)
                flat_name = f"{nb_path.stem}_{os.path.basename(img_path)}"
                dst_img = images_dir / flat_name
                shutil.copy2(src_img, dst_img)
                return f"!{match.group(1)}(images/{flat_name})"
            # Update image links: ![alt](path)
            import re
            md_content_new = re.sub(r'(!\[[^\]]*\])\(([^)]+)\)', copy_and_update, cell.source)
            if md_content_new != cell.source:
                cell.source = md_content_new
                changed = True
        if changed:
            nbformat.write(nb_data, str(nb_path))
            print(f"[INFO] Updated image links in notebook: {nb_path}")

    # Step 3: Convert all notebooks to HTML and copy to docs/
    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        html_path = docs_dir / html_name
        print(f"Converting {nb} to {html_path}")
        run(['jupyter', 'nbconvert', '--to', 'html', str(nb), '--output', html_name, '--output-dir', str(docs_dir)])

    print("All notebooks converted to HTML and copied to docs/.")
    print("You can now deploy docs/ as a static website (e.g., with GitHub Pages).")

if __name__ == '__main__':
    main()
