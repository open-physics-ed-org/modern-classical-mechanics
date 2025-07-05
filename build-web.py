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
            # --- Admonition conversion ---
            # Preprocess code-fence style admonitions (```{tip} ... ```) to HTML before nbconvert
            orig_src = cell.source
            # Only process if code-fence style admonition is present
            if re.search(r'```\{(admonition|tip|note|warning|caution|important|hint|danger|error|success|question|quote|seealso)\}', orig_src):
                # Replace all code-fence style admonitions in the markdown cell
                def codefence_admonition(match):
                    ad_type = match.group(1).strip().lower()
                    title = match.group(2)
                    content = match.group(3)
                    if not title or title.strip() == '':
                        title = ad_type.title()
                    content = content.strip('\n')
                    return (
                        f'<div class="admonition {ad_type}" role="region" aria-label="{ad_type.title()}">' 
                        f'<div class="admonition-title">{title}</div>\n{content}\n</div>'
                    )
                new_src = re.sub(
                    r'```\{(admonition|tip|note|warning|caution|important|hint|danger|error|success|question|quote|seealso)\}(?: +([^\n]+))?\n([\s\S]+?)\n```',
                    codefence_admonition, orig_src)
                if new_src != orig_src:
                    cell.source = new_src
                    changed = True
            def update_img_link(match):
                alt_text = match.group(1)
                img_path = match.group(2).strip()
                # --- YOUTUBE THUMBNAIL HANDLING ---
                # 1. Direct YouTube thumbnail URL
                yt_match = re.match(r'https?://img\.youtube\.com/vi/([\w-]{11})/', img_path)
                if yt_match:
                    video_id = yt_match.group(1)
                    local_img_name = f"youtube_{video_id}.jpg"
                    print(f"[DEBUG] Rewriting YouTube thumbnail: {img_path} -> images/{local_img_name}")
                    referenced_images.add((images_dir / local_img_name, images_dir / local_img_name))
                    all_youtube_ids.add(video_id)
                    return f"![{alt_text}](images/{local_img_name})"

                # 2. Mangled YouTube thumbnail (e.g. images/youtube___hqdefault.jpg)
                yt_mangled = re.match(r'images/youtube___(hqdefault|maxresdefault)\.jpg', img_path)
                if yt_mangled:
                    # Try to find a YouTube video ID in the cell source
                    video_id = None
                    # Try to extract from alt_text if it looks like a video ID
                    if re.match(r'^[\w-]{11}$', alt_text):
                        video_id = alt_text
                    # Try to extract from the cell source (look for a YouTube link)
                    if not video_id:
                        yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
                        if yt_links:
                            video_id = yt_links[0]
                    if video_id:
                        local_img_name = f"youtube_{video_id}.jpg"
                        print(f"[DEBUG] Rewriting mangled YouTube thumbnail: {img_path} -> images/{local_img_name}")
                        referenced_images.add((images_dir / local_img_name, images_dir / local_img_name))
                        all_youtube_ids.add(video_id)
                        return f"![{alt_text}](images/{local_img_name})"
                    else:
                        print(f"[WARNING] Could not extract YouTube video ID for mangled thumbnail: {img_path}")
                        # fallback: leave as is
                        return match.group(0)

                # 3. Other mangled YouTube thumbnail (e.g. images/https:__hqdefault.jpg)
                if (img_path.endswith('hqdefault.jpg') or img_path.endswith('maxresdefault.jpg')) and ('youtube' in img_path or 'http' in img_path or img_path.startswith('images/https')):
                    video_id = None
                    # Try to extract from alt_text if it looks like a video ID
                    if re.match(r'^[\w-]{11}$', alt_text):
                        video_id = alt_text
                    # Try to extract from the image path
                    if not video_id:
                        m = re.search(r'([\w-]{11})', img_path)
                        if m:
                            video_id = m.group(1)
                    # Try to extract from the cell source (look for a YouTube link)
                    if not video_id:
                        yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
                        if yt_links:
                            video_id = yt_links[0]
                    if video_id:
                        local_img_name = f"youtube_{video_id}.jpg"
                        print(f"[DEBUG] Rewriting mangled YouTube thumbnail: {img_path} -> images/{local_img_name}")
                        referenced_images.add((images_dir / local_img_name, images_dir / local_img_name))
                        all_youtube_ids.add(video_id)
                        return f"![{alt_text}](images/{local_img_name})"
                    else:
                        print(f"[WARNING] Could not extract YouTube video ID for mangled thumbnail: {img_path}")
                        return match.group(0)

                # --- NORMAL IMAGE HANDLING ---
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
                # Avoid copying a file onto itself
                try:
                    if os.path.abspath(src_img) != os.path.abspath(dest_img):
                        shutil.copy2(src_img, dest_img)
                except Exception as e:
                    print(f"[ERROR] Copying {src_img} to {dest_img}: {e}")
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
    import json
    css_path = repo_root / 'static' / 'css' / 'main.css'
    css_rel = 'css/main.css'

    # --- Load menu structure from _menu.yml using basic_yaml2json.py ---
    menu_yml = repo_root / '_menu.yml'
    menu_data = None
    if menu_yml.exists():
        import subprocess
        try:
            result = subprocess.run([
                'python3', str(repo_root / 'basic_yaml2json.py'), str(menu_yml)
            ], capture_output=True, check=True)
            menu_json = result.stdout.decode('utf-8')
            menu_obj = json.loads(menu_json)
            if isinstance(menu_obj, dict) and 'menu' in menu_obj:
                menu_data = menu_obj['menu']
            else:
                menu_data = menu_obj
        except Exception as e:
            print(f'[ERROR] Could not convert _menu.yml to JSON using basic_yaml2json.py: {e}')
            menu_data = None

    def build_menu_html(menu_items, level=0):
        html = ''
        if not menu_items:
            return html
        html += f'<ul class="menu-level-{level}">'  # Add class for styling
        for item in menu_items:
            title = item.get('title', '')
            path = item.get('path', None)
            children = item.get('children', None)
            html += '<li>'
            if path:
                html += f'<a href="{path}">{title}</a>'
            else:
                html += f'<span>{title}</span>'
            if children:
                html += build_menu_html(children, level+1)
            html += '</li>'
        html += '</ul>'
        return html

    def get_nav_html():
        nav_html = ''
        if menu_data:
            nav_html = build_menu_html(menu_data)
        else:
            nav_html = '''<ul class="menu-level-0">
                <li><a href="index.html">Home</a></li>
                <li><a href="01_notes.html">Chapters</a></li>
                <li><a href="resources.html">Resources</a></li>
                <li><a href="about.html">About</a></li>
            </ul>'''
        nav_html += '<button class="toggle-dark" aria-label="Toggle dark/light mode" onclick="document.body.classList.toggle(\'dark\')">🌗</button>'
        return f'<nav>{nav_html}</nav>'

    def get_html_template(title, body):
        nav_html = get_nav_html()
        return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title}</title>
      <link href="css/main.css" rel="stylesheet">
      <script src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' defer></script>
    </head>
    <body class="dark">
      {nav_html}
      <div class="container">
        <main id="main-content">
          {body}
        </main>
      </div>
      <footer>
        <p>&copy; Modern Classical Mechanics. All rights reserved.</p>
      </footer>
    </body>
    </html>"""

    # --- Process intro.md as index.html ---
    intro_md = repo_root / 'intro.md'
    index_html_path = build_dir / 'index.html'
    if intro_md.exists():
        try:
            import markdown
        except ImportError:
            import sys
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(intro_md, 'r', encoding='utf-8') as f:
            intro_content = f.read()
        main_html = markdown.markdown(intro_content, extensions=['extra', 'toc', 'admonition'])
        card_grid = '''<section class="card-grid" aria-label="Main sections">
  <div class="card" tabindex="0"><h2><a href="01_notes.html">Chapters</a></h2><p>Lecture notes and weekly content</p></div>
  <div class="card" tabindex="0"><h2><a href="resources.html">Resources</a></h2><p>Reference materials, links, and tools</p></div>
  <div class="card" tabindex="0"><h2><a href="about.html">About</a></h2><p>Course info, instructor, and policies</p></div>
</section>'''
        body = f'<div class="markdown-body">{main_html}{card_grid}</div>'
        html = get_html_template("Modern Classical Mechanics", body)
        with open(index_html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # --- Process all notebooks as HTML with the same template ---
    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        html_path = build_dir / html_name
        exporter = HTMLExporter()
        (body, resources) = exporter.from_filename(str(nb))
        # Do not convert admonitions in HTML body; already handled in markdown preprocessing
        body = f'<div class="markdown-body">{body}</div>'
        title = nb.stem.replace('_', ' ').title()
        html = get_html_template(title, body)
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
    shutil.copy2(css_path, docs_css_dir / 'main.css')
    images_docs_dir = docs_dir / 'images'
    images_docs_dir.mkdir(parents=True, exist_ok=True)
    for img_file in images_dir.glob('*'):
        shutil.copy2(img_file, images_docs_dir / img_file.name)

    print("All notebooks converted to HTML and copied to docs/ with images, CSS, and accessible menu.")

if __name__ == '__main__':
    main()