#!/usr/bin/env python3
import os
import shutil
import re
import hashlib
import requests
import nbformat
from pathlib import Path
from nbconvert import HTMLExporter

def flatten_image_name(rel_path):
    return rel_path.replace('/', '_').replace('\\', '_')

def fetch_youtube_thumbnail(video_id, dest_path):
    urls = [
        f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    ]
    for url in urls:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            with open(dest_path, 'wb') as f:
                f.write(resp.content)
            return True
        except Exception:
            continue
    return False

def main():
    repo_root = Path(__file__).parent.resolve()
    notebooks_dir = repo_root / 'notebooks'
    docs_dir = repo_root / 'docs'
    build_dir = repo_root / '_build' / 'html'
    build_dir.mkdir(parents=True, exist_ok=True)

    # Ensure docs/ exists and .nojekyll for GitHub Pages
    docs_dir.mkdir(parents=True, exist_ok=True)
    nojekyll = docs_dir / '.nojekyll'
    if not nojekyll.exists():
        nojekyll.touch()


    # 1. Copy all images (notebook-prefixed name) from notebooks/images/** to _build/html/images and docs/images
    images_root = notebooks_dir / 'images'
    all_image_files = list(images_root.rglob('*'))
    images_dir = build_dir / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)

    # 1. For each notebook, update image references and copy images using a path-derived prefix
    def path_to_output_name(rel_path):
        print(f"[DEBUG:path_to_output_name] Input rel_path: {rel_path}")
        # Remove any leading 'images/'
        if rel_path.startswith('images/'):
            rel_path = rel_path[7:]
            print(f"[DEBUG:path_to_output_name] Stripped 'images/': {rel_path}")
        # Use the first two path components as prefix if possible
        parts = rel_path.split('/')
        print(f"[DEBUG:path_to_output_name] parts: {parts}")
        if len(parts) >= 3:
            # e.g., notes/week1/box_fbd.png -> 01_notes_box_fbd.png
            prefix = parts[0]  # e.g., 'notes'
            week = parts[1]    # e.g., 'week1'
            base = parts[-1]
            print(f"[DEBUG:path_to_output_name] prefix: {prefix}, week: {week}, base: {base}")
            # Try to extract NN from week (e.g., week1 -> 01)
            m = re.match(r'week(\d+)', week)
            if m:
                nn = m.group(1).zfill(2)
                out_name = f"{nn}_{prefix}_{base}"
                print(f"[DEBUG:path_to_output_name] Matched week: {week} -> nn: {nn}, out_name: {out_name}")
            else:
                out_name = f"{prefix}_{week}_{base}"
                print(f"[DEBUG:path_to_output_name] No week match, out_name: {out_name}")
        else:
            out_name = rel_path.replace('/', '_')
            print(f"[DEBUG:path_to_output_name] Fallback out_name: {out_name}")
        return out_name


    # --- Aggregate missing images and YouTube thumbnails across all notebooks ---
    all_missing_images = set()
    all_youtube_ids = set()

    for nb_path in notebooks_dir.glob('*.ipynb'):
        nb_data = nbformat.read(str(nb_path), as_version=4)
        changed = False
        referenced_images = set()
        for cell in nb_data.cells:
            if cell.cell_type != 'markdown':
                continue
            def update_img_link(match):
                alt_text = match.group(1)
                img_path = match.group(2).strip()
                img_path_clean = img_path
                if img_path_clean.startswith('images/'):
                    img_path_clean = img_path_clean[7:]
                real_img_path = images_root / img_path_clean
                if not real_img_path.exists():
                    possible = nb_path.parent / img_path
                    if possible.exists():
                        try:
                            rel_path = possible.relative_to(images_root)
                        except ValueError:
                            rel_path = img_path_clean
                        real_img_path = images_root / rel_path
                    else:
                        rel_path = img_path_clean
                else:
                    rel_path = img_path_clean
                new_img_name = path_to_output_name(str(rel_path))
                print(f"[DEBUG] Notebook: {nb_path.name} | Markdown ref: {img_path} | resolved rel_path: {rel_path} | real_img_path: {real_img_path} | output: images/{new_img_name}")
                referenced_images.add((real_img_path, images_dir / new_img_name))
                # Track missing images
                if not real_img_path.exists():
                    all_missing_images.add((str(real_img_path), str(nb_path), img_path))
                    # Check for YouTube thumbnail pattern
                    yt_match = re.match(r'https?://img\.youtube\.com/vi/([\w-]{11})/', img_path)
                    if yt_match:
                        all_youtube_ids.add(yt_match.group(1))
                return f"![{alt_text}](images/{new_img_name})"
            new_src = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', update_img_link, cell.source)
            # Also look for YouTube links in plain text
            yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
            for video_id in yt_links:
                all_youtube_ids.add(video_id)
            if new_src != cell.source:
                cell.source = new_src
                changed = True
        if changed:
            nbformat.write(nb_data, str(nb_path))
            print(f"[INFO] Updated image links in notebook: {nb_path}")
        # Copy all referenced images for this notebook
        for src_img, dest_img in referenced_images:
            if src_img.exists():
                dest_img.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_img, dest_img)
            else:
                print(f"[WARNING] Image not found: {src_img}")

    # --- Summary of missing images ---
    if all_missing_images:
        print("\n[SUMMARY] Missing images across all notebooks:")
        for missing_path, nb_name, orig_ref in sorted(all_missing_images):
            print(f"  - {missing_path} (notebook: {nb_name}, original ref: {orig_ref})")
    else:
        print("[SUMMARY] No missing images!")

    # --- Fetch all unique YouTube thumbnails ---
    if all_youtube_ids:
        print("\n[INFO] Attempting to fetch YouTube thumbnails:")
        for video_id in sorted(all_youtube_ids):
            dest_path = images_dir / f"youtube_{video_id}.jpg"
            if not dest_path.exists():
                print(f"  Fetching thumbnail for video ID: {video_id} -> {dest_path}")
                ok = fetch_youtube_thumbnail(video_id, dest_path)
                if ok:
                    print(f"    [OK] Downloaded thumbnail for {video_id}")
                else:
                    print(f"    [FAIL] Could not fetch thumbnail for {video_id}")
            else:
                print(f"  [SKIP] Thumbnail already exists for {video_id}")
    else:
        print("[INFO] No YouTube thumbnails to fetch.")


    # (Removed redundant second pass for flattening image names)

    # 4. Convert notebooks to HTML with custom CSS and template
    css_path = repo_root / 'static' / 'css' / 'book.css'
    css_rel = 'css/book.css'
    html_template = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{{{title}}}}</title>
  <link href="{css_rel}" rel="stylesheet">
  <script>
    function toggleDark() {{
      document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
    }}
    if (localStorage.getItem('theme') === 'dark') document.documentElement.classList.add('dark');
  </script>
</head>
<body>
  <button class="toggle-dark" onclick="toggleDark()">🌗</button>
  <div class="container">
    {{{{body}}}}
  </div>
</body>
</html>'''
    build_css_dir = build_dir / 'css'
    build_css_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(css_path, build_css_dir / 'book.css')

    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        html_path = build_dir / html_name
        exporter = HTMLExporter()
        (body, resources) = exporter.from_filename(str(nb))
        title = nb.stem.replace('_', ' ').title()
        html = html_template.replace('{{title}}', title).replace('{{body}}', body)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # 5. Copy everything to docs/
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
    shutil.copy2(css_path, docs_css_dir / 'book.css')
    images_docs_dir = docs_dir / 'images'
    images_docs_dir.mkdir(parents=True, exist_ok=True)
    for img_file in images_dir.glob('*'):
        shutil.copy2(img_file, images_docs_dir / img_file.name)

    print("All notebooks converted to HTML and copied to docs/ with images and CSS.")

if __name__ == '__main__':
    main()