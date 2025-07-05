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
    build_dir = repo_root / '_build' / 'html'
    build_dir.mkdir(parents=True, exist_ok=True)

    # Ensure .nojekyll for GitHub Pages (will be copied at the end)
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
    images_dir = build_dir / 'images'
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

    # Step 3: Convert all notebooks to HTML using a custom template and copy to _build/html/
    template_path = repo_root / 'static' / 'html_template.html'
    if not template_path.exists():
        with open(template_path, 'w') as f:
            f.write('''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="/static/css/tailwind.css" rel="stylesheet">
  <script>
    function toggleDark() {
      document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
    }
    if (localStorage.getItem('theme') === 'dark') document.documentElement.classList.add('dark');
  </script>
</head>
<body class="bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100 transition-colors duration-200">
  <button class="toggle-dark" onclick="toggleDark()">🌗</button>
  <div class="container mx-auto px-4 max-w-3xl">
    {body}
  </div>
</body>
</html>''')
        print(f"[INFO] Created default HTML template at {template_path}")

    import nbconvert
    from nbconvert import HTMLExporter
    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        html_path = build_dir / html_name
        print(f"Converting {nb} to {html_path} with custom template")
        exporter = HTMLExporter()
        (body, resources) = exporter.from_filename(str(nb))
        # Extract title from notebook filename or metadata
        title = nb.stem.replace('_', ' ').title()
        with open(template_path) as f:
            template = f.read()
        html = template.replace('{title}', title).replace('{body}', body)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # Copy static/css/book.css to _build/html/css/
    static_css = repo_root / 'static' / 'css' / 'book.css'
    build_css_dir = build_dir / 'css'
    build_css_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(static_css, build_css_dir / 'book.css')

    # Copy everything from _build/html/ to docs/, preserving .nojekyll
    print("Copying _build/html/ to docs/ (preserving .nojekyll)...")
    docs_css_dir = docs_dir / 'css'
    docs_css_dir.mkdir(parents=True, exist_ok=True)
    for item in docs_dir.iterdir():
        if item.name == '.nojekyll':
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    for item in build_dir.iterdir():
        dest = docs_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)
    # Copy static/css/book.css to docs/css/
    shutil.copy2(static_css, docs_css_dir / 'book.css')

    print("All notebooks converted to HTML and copied to docs/.")
    print("You can now deploy docs/ as a static website (e.g., with GitHub Pages).")

if __name__ == '__main__':
    main()
