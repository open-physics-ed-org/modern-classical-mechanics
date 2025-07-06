#!/usr/bin/env python3
import os
import shutil
import re
import hashlib
import requests
import nbformat
from pathlib import Path
from nbconvert import HTMLExporter

import string
def flatten_image_name(rel_path):
    # Lowercase, replace / and \ with _, remove spaces, keep only a-z0-9-_.
    name = rel_path.replace('/', '_').replace('\\', '_').lower().replace(' ', '_')
    allowed = set(string.ascii_lowercase + string.digits + '-_.')
    return ''.join(c for c in name if c in allowed)

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


    # --- Load menu structure from _menu.yml using basic_yaml2json.py ---
    import json
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

    # --- Section-aware image flattening ---
    # Support images in both notebooks/images/ and project-root images/
    images_root_candidates = [repo_root / 'images', notebooks_dir / 'images']
    images_dir = build_dir / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)

    # Helper: Map notebook HTML name to menu section (e.g., 'chapters', 'activities')
    def get_section_for_notebook(html_name, menu_data):
        def search_menu(items, section=None):
            for item in items:
                if 'children' in item:
                    found = search_menu(item['children'], item['title'].lower())
                    if found:
                        return found
                if 'path' in item and item['path'] == html_name:
                    return section or item['title'].lower()
            return None
        return search_menu(menu_data) if menu_data else None

    # Section-aware output image path: images/<section>/<filename>
    def path_to_output_name(rel_path, section):
        # Remove any leading 'images/'
        if rel_path.startswith('images/'):
            rel_path = rel_path[7:]
        filename = os.path.basename(rel_path)
        # Section folder (lowercase, fallback to 'other')
        section_folder = section.lower() if section else 'other'
        return f"{section_folder}/{filename}"

    # Ensure subfolders for each section
    def ensure_section_dir(section):
        section_folder = section.lower() if section else 'other'
        section_dir = images_dir / section_folder
        section_dir.mkdir(parents=True, exist_ok=True)
        return section_dir


    # --- Aggregate missing images and YouTube thumbnails across all notebooks ---
    all_missing_images = set()
    all_youtube_ids = set()
    all_section_image_map = {}  # {html_name: section}
    # Precompute menu mapping for all notebooks
    menu_html_names = {}
    if menu_data:
        def collect_paths(items, section=None):
            for item in items:
                if 'children' in item:
                    collect_paths(item['children'], item['title'].lower())
                if 'path' in item:
                    menu_html_names[item['path']] = section or item['title'].lower()
        collect_paths(menu_data)

    for nb_path in notebooks_dir.glob('*.ipynb'):
        html_name = nb_path.with_suffix('.html').name
        section = menu_html_names.get(html_name, 'other')
        all_section_image_map[html_name] = section
        section_dir = ensure_section_dir(section)
        nb_data = nbformat.read(str(nb_path), as_version=4)
        referenced_images = set()
        for cell in nb_data.cells:
            if cell.cell_type != 'markdown':
                continue
            def update_img_link(match):
                alt_text = match.group(1)
                img_path = match.group(2).strip()
                # --- YOUTUBE THUMBNAIL HANDLING ---
                yt_match = re.match(r'https?://img\.youtube\.com/vi/([\w-]{11})/', img_path)
                if yt_match:
                    video_id = yt_match.group(1)
                    local_img_name = f"youtube_{video_id}.jpg"
                    referenced_images.add((images_dir / section.lower() / local_img_name, images_dir / section.lower() / local_img_name, f"{section.lower()}/{local_img_name}"))
                    all_youtube_ids.add(video_id)
                    return
                yt_mangled = re.match(r'images/youtube___(hqdefault|maxresdefault)\.jpg', img_path)
                if yt_mangled:
                    video_id = None
                    if re.match(r'^[\w-]{11}$', alt_text):
                        video_id = alt_text
                    if not video_id:
                        yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
                        if yt_links:
                            video_id = yt_links[0]
                    if video_id:
                        local_img_name = f"youtube_{video_id}.jpg"
                        referenced_images.add((images_dir / section.lower() / local_img_name, images_dir / section.lower() / local_img_name, f"{section.lower()}/{local_img_name}"))
                        all_youtube_ids.add(video_id)
                    return
                if (img_path.endswith('hqdefault.jpg') or img_path.endswith('maxresdefault.jpg')) and ('youtube' in img_path or 'http' in img_path or img_path.startswith('images/https')):
                    video_id = None
                    if re.match(r'^[\w-]{11}$', alt_text):
                        video_id = alt_text
                    if not video_id:
                        m = re.search(r'([\w-]{11})', img_path)
                        if m:
                            video_id = m.group(1)
                    if not video_id:
                        yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
                        if yt_links:
                            video_id = yt_links[0]
                    if video_id:
                        local_img_name = f"youtube_{video_id}.jpg"
                        referenced_images.add((images_dir / section.lower() / local_img_name, images_dir / section.lower() / local_img_name, f"{section.lower()}/{local_img_name}"))
                        all_youtube_ids.add(video_id)
                    return
                # --- NORMAL IMAGE HANDLING ---
                img_path_clean = img_path
                if img_path_clean.startswith('images/'):
                    img_path_clean = img_path_clean[7:]
                if img_path_clean.startswith('.._images_'):
                    clean_name = img_path_clean.replace('.._images_', '', 1)
                    search_names = [clean_name, img_path_clean]
                else:
                    clean_name = img_path_clean
                    search_names = [img_path_clean]
                found = False
                real_img_path = None
                # Try all possible image roots (project root images/, notebooks/images/)
                for name in search_names:
                    for images_root in images_root_candidates:
                        candidate = images_root / name
                        if candidate.exists():
                            real_img_path = candidate
                            found = True
                            break
                    if found:
                        break
                # Fallback: search all section subfolders for a matching filename
                if not found:
                    for images_root in images_root_candidates:
                        for section_dir in images_root.iterdir():
                            if section_dir.is_dir():
                                candidate = section_dir / os.path.basename(clean_name)
                                if candidate.exists():
                                    real_img_path = candidate
                                    found = True
                                    break
                        if found:
                            break
                # fallback: try _images folders
                if not found:
                    for name in search_names:
                        for fallback_root in [notebooks_dir / '_images', build_dir / '_images', repo_root / '_images']:
                            candidate = fallback_root / name
                            if candidate.exists():
                                real_img_path = candidate
                                found = True
                                break
                        if found:
                            break
                if not found:
                    # fallback: just use the first images_root
                    real_img_path = images_root_candidates[0] / img_path_clean
                out_img_name = os.path.basename(clean_name)
                new_img_name = path_to_output_name(str(out_img_name), section)
                referenced_images.add((real_img_path, images_dir / new_img_name, new_img_name))
                if not found:
                    all_missing_images.add((str(real_img_path), str(nb_path), img_path))
            re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', update_img_link, cell.source)
            yt_links = re.findall(r'(?:youtube.com/watch\?v=|youtu.be/)([\w-]{11})', cell.source)
            for video_id in yt_links:
                all_youtube_ids.add(video_id)
        for src_img, dest_img, new_img_name in referenced_images:
            if src_img.exists():
                dest_img.parent.mkdir(parents=True, exist_ok=True)
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
        # Top-level: horizontal menu
        if level == 0:
            html += '<ul class="site-nav-menu">'
        else:
            html += f'<ul class="dropdown-menu menu-level-{level}">'  # Dropdown for children
        for item in menu_items:
            title = item.get('title', '')
            path = item.get('path', None)
            children = item.get('children', None)
            html += '<li>'
            if path:
                html += f'<a href="{path}">{title}</a>'
            else:
                html += f'<span tabindex="0">{title}</span>'
            if children:
                html += build_menu_html(children, level+1)
            html += '</li>'
        html += '</ul>'
        return html

    def get_nav_html():
        # Accessible nav: desktop and mobile, with ARIA and toggle
        nav_html = '<button class="site-nav-toggle" aria-label="Open menu" aria-controls="site-nav-menu" aria-expanded="false" tabindex="0">☰</button>'
        # Use menu_data if available, else fallback
        if menu_data:
            nav_html += build_menu_html(menu_data)
        else:
            nav_html += '<!-- Menu data not available, fallback menu here -->'
        nav_html += """
<button class="toggle-dark" aria-label="Toggle dark/light mode" onclick="document.body.classList.toggle('dark')">🌗</button>
<script>
document.addEventListener('DOMContentLoaded',function(){
  var nav = document.getElementById('site-nav');
  var menu = document.getElementById('site-nav-menu');
  var toggle = document.querySelector('.site-nav-toggle');
  if(menu && toggle){
    toggle.addEventListener('click',function(){
      var expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded',!expanded);
      menu.classList.toggle('open');
    });
    toggle.addEventListener('keydown',function(e){
      if(e.key==='Enter'||e.key===' '){
        e.preventDefault();
        toggle.click();
      }
    });
    // Keyboard nav for menu items
    menu.querySelectorAll('a,span').forEach(function(el){
      el.setAttribute('tabindex','0');
    });
    // Dropdown ARIA
    menu.querySelectorAll('a[aria-haspopup="true"]').forEach(function(link){
      link.addEventListener('click',function(e){
        var expanded = link.getAttribute('aria-expanded') === 'true';
        link.setAttribute('aria-expanded',!expanded);
        var submenu = document.getElementById(link.getAttribute('aria-controls'));
        if(submenu) submenu.style.display = expanded ? 'none' : 'block';
        e.preventDefault();
      });
      link.addEventListener('keydown',function(e){
        if(e.key==='Enter'||e.key===' '){
          e.preventDefault();
          link.click();
        }
      });
    });
  }
});
</script>
"""
        return nav_html

    def get_html_template(title, body):
        nav_html = get_nav_html()
        # Read the book title from _config.yml
        import yaml
        config_path = Path(__file__).parent / '_config.yml'
        book_title = title
        footer_html = None
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                if 'title' in config:
                    book_title = config['title']
                if 'footer' in config:
                    footer_html = config['footer']
        if not footer_html:
            footer_html = f"&copy; {book_title}. All rights reserved."
        # Center the title and remove extra white header
        # No override style injected; main.css controls all site appearance
        return f"""<!DOCTYPE html>
    <html lang=\"en\">\n    <head>\n      <meta charset=\"UTF-8\">\n      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n      <title>{book_title}</title>\n      <link href=\"css/main.css\" rel=\"stylesheet\">\n      <script src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' defer></script>\n    </head>\n    <body class=\"dark\">\n      <header class=\"site-header\">\n        <h1 class=\"site-title\">{book_title}</h1>\n      </header>\n      <nav class=\"site-nav\" id=\"site-nav\">{nav_html}</nav>\n      <div class=\"layout-main\">\n        <div class=\"container\">\n          <main id=\"main-content\">\n            {body}\n          </main>\n        </div>\n      </div>\n      <footer>\n        <p>{footer_html}</p>\n      </footer>\n    </body>\n    </html>"""

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
        # --- Load cards from _cards.yml ---
        import yaml
        cards_yml = repo_root / '_cards.yml'
        cards = []
        if cards_yml.exists():
            with open(cards_yml, 'r', encoding='utf-8') as f:
                try:
                    cards_data = yaml.safe_load(f)
                    if cards_data and 'cards' in cards_data and isinstance(cards_data['cards'], list):
                        cards = cards_data['cards']
                except Exception as e:
                    print(f"[ERROR] Could not parse _cards.yml: {e}")
        def build_card_grid(cards):
            if not cards:
                return ''
            html = '<section class="card-grid" aria-label="Main sections">\n'
            for card in cards:
                title = card.get('title', '')
                context = card.get('context', '')
                link = card.get('link', '#')
                html += f'  <div class="card" tabindex="0"><h2><a href="{link}">{title}</a></h2><p>{context}</p></div>\n'
            html += '</section>\n'
            return html
        card_grid = build_card_grid(cards)
        body = f'<div class="markdown-body">{main_html}{card_grid}</div>'
        html = get_html_template("Modern Classical Mechanics", body)
        with open(index_html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # --- Build chapters.html dynamically from _menu.yml ---
    chapters_html_path = build_dir / 'chapters.html'
    def build_chapters_page(menu_data):
        # Find the 'Chapters' section in menu_data
        chapters = None
        for item in menu_data:
            if item.get('title', '').lower() == 'chapters' and 'children' in item:
                chapters = item['children']
                break
        if not chapters:
            return '<p>No chapters found in menu.</p>'
        html = '<section class="card-grid chapters-grid" aria-label="Chapters">'
        docs_dir = Path(__file__).parent / 'docs'
        for ch in chapters:
            title = ch.get('title', '')
            path = ch.get('path', '')
            thumb_img = None
            thumb_alt = ''
            html_path = docs_dir / path
            section = 'chapters'
            # Try to find the first flat image in the corresponding section folder (ignore .._.._ prefix)
            section_img_dir = docs_dir / 'images' / section
            img_file = None
            if section_img_dir.exists():
                for f in sorted(section_img_dir.iterdir()):
                    if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg'] and not f.name.startswith('.._.._'):
                        img_file = f
                        break
            if img_file:
                thumb_img = f'images/{section}/{img_file.name}'
                thumb_alt = title
            else:
                # fallback to old logic (scan HTML)
                if html_path.exists():
                    try:
                        with open(html_path, 'r', encoding='utf-8') as f:
                            for line in f:
                                m = re.search(r'<img [^>]*src=["\']([^"\']+)["\'][^>]*', line)
                                if m:
                                    thumb_img = m.group(1)
                                    alt_m = re.search(r'alt=["\']([^"\']*)["\']', line)
                                    if alt_m:
                                        thumb_alt = alt_m.group(1)
                                    break
                    except Exception as e:
                        print(f"[WARN] Could not read {html_path}: {e}")
            # Fallback: no image found
            if thumb_img:
                img_html = f'<a href="{path}"><img class="chapter-thumb" src="{thumb_img}" alt="{thumb_alt}" loading="lazy" style="max-width:100%;max-height:140px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,0.08);margin-bottom:1em;"></a>'
            else:
                img_html = ''
            html += f'''<div class="card" tabindex="0">{img_html}<h2><a href="{path}">{title}</a></h2></div>'''
        html += '</section>'
        return html
    if menu_data:
        chapters_body = build_chapters_page(menu_data)
        chapters_html = get_html_template("Chapters", chapters_body)
        with open(chapters_html_path, 'w', encoding='utf-8') as f:
            f.write(chapters_html)

    # --- Process all notebooks as HTML with the same template, rewriting image links to section subfolders ---
    # Build a mapping from all copied images: filename -> (section, relpath)
    copied_images = {}
    for section_dir in images_dir.iterdir():
        if section_dir.is_dir():
            section = section_dir.name
            for img_file in section_dir.iterdir():
                if img_file.is_file():
                    copied_images[img_file.name] = (section, f'images/{section}/{img_file.name}')

    for nb in notebooks_dir.glob('*.ipynb'):
        html_name = nb.with_suffix('.html').name
        section = menu_html_names.get(html_name, 'other')
        html_path = build_dir / html_name
        exporter = HTMLExporter()
        (body, resources) = exporter.from_filename(str(nb))
        # Rewrite image links in HTML to point to images/<section>/filename, using copied_images mapping
        def rewrite_img_src(match):
            src = match.group(1)
            filename = os.path.basename(src)
            if filename in copied_images:
                new_section, new_rel = copied_images[filename]
                return f'src="{new_rel}"'
            return match.group(0)
        body = re.sub(r'src=["\']([^"\']+)["\']', rewrite_img_src, body)
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
    # Copy only main.css to docs/css and _build/html/css
    docs_css_dir.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(css_path, docs_css_dir / 'main.css')
    except Exception as e:
        print(f"[ERROR] Failed to copy main.css to {docs_css_dir}: {e}")
        raise
    build_css_dir = build_dir / 'css'
    build_css_dir.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(css_path, build_css_dir / 'main.css')
    except Exception as e:
        print(f"[ERROR] Failed to copy main.css to {build_css_dir}: {e}")
        raise
    # Copy all images to docs/images/<section>/
    images_docs_dir = docs_dir / 'images'
    images_docs_dir.mkdir(parents=True, exist_ok=True)
    for section_dir in images_dir.iterdir():
        if section_dir.is_dir():
            dest_section_dir = images_docs_dir / section_dir.name
            dest_section_dir.mkdir(parents=True, exist_ok=True)
            for img_file in section_dir.iterdir():
                if img_file.is_file():
                    shutil.copy2(img_file, dest_section_dir / img_file.name)

    # --- Check: verify all referenced images exist in docs/images/ ---
    missing_in_docs = []
    for html_name in all_section_image_map.keys():
        html_path = docs_dir / html_name
        if not html_path.exists():
            continue
        with open(html_path, 'r', encoding='utf-8') as f:
            for line in f:
                for m in re.finditer(r'src=["\'](images/[^/"\']+)["\']', line):
                    img_rel = m.group(1)
                    img_abs = docs_dir / img_rel
                    if not img_abs.exists():
                        missing_in_docs.append((html_name, img_rel))
    if missing_in_docs:
        print("[CHECK] Missing images in docs HTML output:")
        for html_name, img_rel in missing_in_docs:
            print(f"  - {img_rel} (referenced in {html_name})")
    else:
        print("[CHECK] All referenced images exist in docs output.")

    print("All notebooks converted to HTML and copied to docs/ with sectioned images, CSS, and accessible menu.")

if __name__ == '__main__':
    main()