# --- Build resources.html from resources.md and about.html from about.md ---
    # (Code moved inside main() after all variables are defined)
#!/usr/bin/env python3
from pathlib import Path
# --- Global paths (needed by all functions) ---
repo_root = Path(__file__).parent.resolve()
docs_dir = repo_root / 'docs'
build_dir = repo_root / '_build' / 'wcag-html'
notebooks_dir = repo_root / 'content' / 'notebooks'
build_dir.mkdir(parents=True, exist_ok=True)
docs_dir.mkdir(parents=True, exist_ok=True)
nojekyll = docs_dir / '.nojekyll'
if not nojekyll.exists():
    nojekyll.touch()
import os
import shutil
import hashlib
import requests
import nbformat
from pathlib import Path
from nbconvert import HTMLExporter
import bs4
import sys
import re
import subprocess
import string
import yaml
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
    # --- Run theme_to_css.py before any HTML build ---
    theme_script = str(Path(__file__).parent / 'theme_to_css.py')
    if Path(theme_script).exists():
        print("[THEME] Generating CSS from YAML themes...")
        result = subprocess.run([sys.executable, theme_script], capture_output=True, text=True)
        if result.returncode != 0:
            print("[THEME][ERROR] theme_to_css.py failed:")
            print(result.stdout)
            print(result.stderr)
        else:
            print("[THEME] CSS generation complete.")
    else:
        print("[THEME][WARN] theme_to_css.py not found, skipping theme CSS generation.")

    # No argument parsing: always build everything (HTML, all notebooks, all pages)
    # Remove Jupyter/nbconvert markup from all HTML in docs/ (always after build)
    def clean_html_files_in_docs():
        try:
            import bs4
        except ImportError:
            print("[ERROR] The 'bs4' package is required. Install it with 'pip install beautifulsoup4'.")
            import sys
            sys.exit(1)
        import re
        docs_dir = Path(__file__).parent / 'docs'
        html_files = list(docs_dir.glob('*.html'))
        print(f"[CLEAN] Processing {len(html_files)} HTML files in docs/ ...")
        for html_path in html_files:
            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            # Remove all Jupyter/nbconvert classes and data attributes
            for tag in soup.find_all(True):
                # Remove classes starting with jp-, nb-, or nbconvert-
                if tag.has_attr('class'):
                    tag['class'] = [c for c in tag['class'] if not (c.startswith('jp-') or c.startswith('nb-') or c.startswith('nbconvert'))]
                    if not tag['class']:
                        del tag['class']
                # Remove data attributes from nbconvert/jupyter
                for attr in list(tag.attrs):
                    if attr.startswith('data-jp-') or attr.startswith('data-nb-') or attr.startswith('data-nbconvert'):
                        del tag[attr]
            # Remove style blocks with Jupyter/nbconvert variables or --jp- CSS vars (robust: check .string and .text)
            for style in soup.find_all('style'):
                style_content = style.string if style.string is not None else style.text
                if style_content and re.search(r'--jp-|nbconvert|nb-', style_content):
                    style.decompose()
            # Remove inline style attributes containing Jupyter/nbconvert CSS variables
            for tag in soup.find_all(True):
                if tag.has_attr('style'):
                    # Remove any --jp-*, nb-*, or nbconvert-* CSS variable definitions from style attribute
                    orig_style = tag['style']
                    # Remove any CSS variable definitions (e.g., --jp-something: ...;)
                    cleaned_style = re.sub(r'(--jp-[\w-]+|nbconvert-[\w-]+|nb-[\w-]+)\s*:[^;]+;?', '', orig_style)
                    # Remove empty style attribute
                    if cleaned_style.strip():
                        tag['style'] = cleaned_style
                    else:
                        del tag['style']

            # Remove literal CSS blocks in the HTML text that reference Jupyter/nbconvert variables, even if not in <style> tags
            # (e.g., .highlight .hll { background-color: var(--jp-cell-editor-active-background); })
            html_str = str(soup)
            # Regex to match CSS blocks containing --jp-, nbconvert, or nb- in their content
            css_block_pattern = re.compile(r'<style[^>]*?>[\s\S]*?</style>', re.IGNORECASE)
            def css_block_cleaner(match):
                css = match.group(0)
                if re.search(r'--jp-|nbconvert|nb-', css):
                    return ''
                return css
            html_str = css_block_pattern.sub(css_block_cleaner, html_str)
            # Remove any inline style attributes containing --jp-, nbconvert, or nb-
            html_str = re.sub(r'style="[^"]*(--jp-|nbconvert|nb-)[^"]*"', '', html_str)
            # Remove any remaining CSS variable definitions in style attributes
            html_str = re.sub(r"(--jp-[a-zA-Z0-9_-]+\s*:[^;\"']+;?)", '', html_str)
            # Remove any remaining class attributes with jp-, nb-, or nbconvert-
            html_str = re.sub(r'class="[^"]*(jp-[^\s"]+|nb-[^\s"]+|nbconvert-[^\s"]+)[^"]*"', '', html_str)

            # Save cleaned HTML (from html_str, not soup)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_str)
            print(f"[CLEAN] Cleaned {html_path.name}")
            # Remove meta tags with nbconvert info (name or content)
            for meta in soup.find_all('meta'):
                if meta.get('name', '').startswith('nbconvert') or meta.get('content', '').startswith('nbconvert'):
                    meta.decompose()
            # Save cleaned HTML
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"[CLEAN] Cleaned {html_path.name}")
        print("[CLEAN] All HTML files in docs/ cleaned of Jupyter/nbconvert markup.")

    # Always build all notebooks listed in _notebooks.yaml (authoritative list)
    notebooks_to_process = None
    notebooks_dir = Path(__file__).parent / 'content/notebooks'
    # Load _notebooks.yaml and build all listed notebooks
    import yaml
    repo_root = Path(__file__).parent.resolve()
    notebooks_yaml = repo_root / '_notebooks.yaml'
    if not notebooks_yaml.exists():
        print("[ERROR] _notebooks.yaml not found!")
        sys.exit(1)
    with open(notebooks_yaml, 'r') as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict) and 'notebooks' in data:
            nb_list = data['notebooks']
        elif isinstance(data, list):
            nb_list = data
        else:
            print("[ERROR] _notebooks.yaml format not recognized.")
            sys.exit(1)
    # Build absolute paths to notebooks (interpret as relative to project root, not notebooks_dir)
    notebooks_to_process = []
    for nb in nb_list:
        nb_path = Path(nb)
        if not nb_path.is_absolute():
            nb_path = repo_root / nb_path
        nb_path = nb_path.resolve()
        if not nb_path.exists():
            print(f"[WARNING] Notebook listed in _notebooks.yaml not found: {nb_path}")
        else:
            notebooks_to_process.append(nb_path)
    if not notebooks_to_process:
        print("[ERROR] No valid notebooks found in _notebooks.yaml.")
        sys.exit(1)


    # --- MAIN BUILD LOGIC: call post_build_cleanup() to process notebooks, images, HTML, etc. ---
    print(f"[BUILD] Processing {len(notebooks_to_process)} notebooks and building site...")
    post_build_cleanup()

    # --- Admonition post-processing for HTML output ---
    # --- Shared emoji mapping for all admonition classes ---
    ADMONITION_EMOJIS = {
        'note': '📝',
        'tip': '💡',
        'warning': '⚠️',
        'caution': '🚧',
        'important': '❗',
        'error': '❌',
        'danger': '�',
        'dangerous': '☠️',
        'hint': '💡',
        'check': '✅',
        'question': '❓',
        'quote': '❝',
        'abstract': '📄',
        'info': 'ℹ️',
        'success': '🎉',
        'failure': '�',
        'bug': '🐞',
        'custom': '🔔',
        'seealso': '🔗',
        'example': '🔍',
        'faq': '❔',
        'summary': '�️',
        'definition': '📘',
        'theorem': '📐',
        'proof': '🧮',
        'exercise': '�️',
        'solution': '🧩',
        'remark': '�',
        'attention': '�',
        'todo': '�️',
        'admonition': '💬',
    }
    def get_admonition_emoji(cls):
        # Use a default emoji (info) for unknown/custom classes
        return ADMONITION_EMOJIS.get(cls.lower(), 'ℹ️')

    def preprocess_custom_admonitions(html):
        # Look for <pre><code class="language-{admonition}"> block:
        def admonition_code_repl(m):
            code = m.group(1)
            print('[DEBUG] Matched <pre><code class="language-{admonition}"> block:')
            print(code)
            lines = code.split('\n', 1)
            if len(lines) == 2:
                title = lines[0].replace('{admonition}', '').strip()
                body = lines[1].strip()
            else:
                title = lines[0].replace('{admonition}', '').strip()
                body = ''
            print(f'[DEBUG] Extracted title: "{title}"')
            print(f'[DEBUG] Extracted body: "{body}"')
            safe_title = re.sub(r'[^a-z0-9_-]+', '', title.lower().replace(' ', '-'))
            emoji = get_admonition_emoji(safe_title)
            # Remove any leftover :class: markup from body
            body = re.sub(r'^:class:.*$', '', body, flags=re.MULTILINE)
            result = f'<div class="admonition {safe_title}"><p class="admonition-title">{emoji} {title}</p>\n{body}</div>'
            print(f'[DEBUG] Replacement HTML: {result}')
            return result
        html = re.sub(
            r'<pre><code class="language-\{admonition\}">\{admonition\}([\s\S]*?)</code></pre>',
            admonition_code_repl,
            html)
        print('[DEBUG] preprocess_custom_admonitions result:')
        print(html[:500])
        return html

    def convert_admonitions(html):
        # Use shared ADMONITION_EMOJIS and get_admonition_emoji

        # 1. Fix nbconvert HTML output: <div class="admonition"><p class="admonition-title">TITLE</p>...</div>
        # Debug counters for each pattern
        nbconvert_div_count = 0
        legacy_codeblock_count = 0
        std_codeblock_count = 0
        myst_block_count = 0

        def fix_admonition_divs(m):
            nonlocal nbconvert_div_count
            nbconvert_div_count += 1
            title = m.group(1).strip()
            content = m.group(2)
            # Remove all :class: ... lines from content (anywhere, not just at start)
            content = re.sub(r'^:class:.*$', '', content, flags=re.MULTILINE)
            content = re.sub(r':class:.*', '', content)
            print(f'[DEBUG] [nbconvert-div] Processing admonition div: title="{title}"')
            print(f'[DEBUG] [nbconvert-div] Raw content: {repr(content[:120])}')
            # Fallback for empty or generic titles: extract first line of content as custom title
            if not title or title.lower() == 'admonition':
                content_lines = content.lstrip().split('\n', 1)
                if content_lines:
                    possible_title = content_lines[0].strip()
                    if 0 < len(possible_title.split()) <= 5 and not possible_title.endswith('.'):
                        custom_title = possible_title
                        rest_content = content_lines[1] if len(content_lines) > 1 else ''
                        safe_title = re.sub(r'[^a-z0-9_-]+', '', custom_title.lower().replace(' ', '-'))
                        class_attr = f"admonition {safe_title}" if safe_title else "admonition"
                        emoji = get_admonition_emoji(safe_title)
                        print(f'[DEBUG] [nbconvert-div] Using emoji "{emoji}" for custom title "{custom_title}" (class: {safe_title})')
                        print(f'[DEBUG] [nbconvert-div] Custom title block: class_attr={class_attr}, rest_content={repr(rest_content[:120])}')
                        title_html = f'<p class="admonition-title">{emoji} {custom_title}</p>'
                        print(f'[DEBUG] [nbconvert-div] Final custom title_html: {title_html}')
                        return f'<div class="{class_attr}">{title_html}\n{rest_content.strip()}</div>'
            if len(title.split()) > 5 or '.' in title:
                content_lines = content.lstrip().split('\n', 1)
                if content_lines:
                    possible_title = content_lines[0].strip()
                    if 0 < len(possible_title.split()) <= 5 and not possible_title.endswith('.'):
                        custom_title = possible_title
                        rest_content = content_lines[1] if len(content_lines) > 1 else ''
                        safe_title = re.sub(r'[^a-z0-9_-]+', '', custom_title.lower().replace(' ', '-'))
                        class_attr = f"admonition {safe_title}" if safe_title else "admonition"
                        emoji = get_admonition_emoji(safe_title)
                        title_html = f'<p class="admonition-title">{emoji} {custom_title}</p>'
                        print(f'[DEBUG] [nbconvert-div] Final custom title_html: {title_html}')
                        return f'<div class="{class_attr}">{title_html}\n{rest_content.strip()}</div>'
            safe_title = re.sub(r'[^a-z0-9_-]+', '', title.lower().split()[0]) if title else 'admonition'
            class_attr = f"admonition {safe_title}" if safe_title else "admonition"
            emoji = get_admonition_emoji(safe_title)
            print(f'[DEBUG] [nbconvert-div] Using emoji "{emoji}" for title "{title}" (class: {safe_title})')
            title_html = f'<p class="admonition-title">{emoji} {title}</p>'
            print(f'[DEBUG] [nbconvert-div] Standard/fallback title_html: {title_html}')
            return f'<div class="{class_attr}">{title_html}\n{content.strip()}</div>'
        # Updated regex: match any <div class="admonition ..."> (with any class list)
        html = re.sub(
            r'<div class="admonition[^"]*">\s*<p class="admonition-title">([^<]*)</p>([\s\S]*?)</div>',
            fix_admonition_divs,
            html)

        # 2. Convert <pre><code class="language-{admonition}">...</code></pre> blocks (legacy, fallback)
        def admonition_repl(m):
            nonlocal legacy_codeblock_count
            legacy_codeblock_count += 1
            title = m.group(1).strip()
            content = m.group(2).lstrip('\n')
            # Remove any leftover :class: markup from content
            content = re.sub(r'^:class:.*$', '', content, flags=re.MULTILINE)
            content = re.sub(r':class:.*', '', content)
            class_match = re.match(r'\s*:class:\s*([a-zA-Z0-9_-]+)\s*\n(.*)', content, re.DOTALL)
            if class_match:
                ad_class = class_match.group(1).strip()
                content = class_match.group(2).lstrip('\n')
            else:
                ad_class = ''
            safe_title = re.sub(r'[^a-z0-9_-]+', '', title.lower().replace(' ', '-'))
            class_attr = f'admonition {ad_class}' if ad_class else f'admonition {safe_title}'
            emoji = get_admonition_emoji(ad_class or safe_title)
            print(f'[DEBUG] [legacy-codeblock] Using emoji "{emoji}" for title "{title}" (class: {ad_class or safe_title})')
            title_html = f'<p class="admonition-title">{emoji} {title}</p>'
            return f'<div class="{class_attr}">{title_html}\n{content.strip()}</div>'
        html = re.sub(
            r'<pre><code class="language-\{admonition\}">\{admonition\}\s*([^\n]*)\n([\s\S]*?)</code></pre>',
            admonition_repl,
            html)

        # 3. Convert <pre><code class="language-{type}">{type} ...</code></pre> blocks (note, warning, tip, etc)
        def std_admonition_repl(m):
            nonlocal std_codeblock_count
            std_codeblock_count += 1
            ad_type = m.group(1)
            extra = m.group(2).strip()
            content = m.group(3).strip()
            emoji = get_admonition_emoji(ad_type)
            print(f'[DEBUG] [std-codeblock] Using emoji "{emoji}" for standard admonition type "{ad_type}"')
            title = f"{ad_type.capitalize()} {extra}".strip()
            return f'<div class="admonition {ad_type}"><p class="admonition-title">{emoji} {title}</p>\n{content}</div>'
        html = re.sub(
            r'<pre><code class="language-\{(note|warning|tip|caution|important|error|danger|hint|check|question|quote|seealso|example|abstract|info|success|failure|bug|custom)\}">\{\1\}([^\n]*)\n([\s\S]*?)</code></pre>',
            std_admonition_repl,
            html)

        # 4. Convert multi-paragraph MyST blocks (with :class: as its own <p>), robustly
        def myst_block_multi_repl(m):
            nonlocal myst_block_count
            myst_block_count += 1
            ad_type = m.group(1)
            extra = m.group(2).strip()
            ad_class = m.group(3).strip()
            content = m.group(4)
            # Remove all <p>:class: ...</p> lines from content
            content = re.sub(r'<p>:class:[^<]*</p>\n?', '', content)
            # Remove any :class: ... lines inside content
            content = re.sub(r':class:.*', '', content)
            content = content.strip()
            safe_type = re.sub(r'[^a-z0-9_-]+', '', ad_class.lower() if ad_class else ad_type.lower())
            emoji = get_admonition_emoji(safe_type)
            title = extra or ad_type.capitalize()
            print(f'[DEBUG] [myst-block-multi] Using emoji "{emoji}" for MyST block type "{ad_type}" (class: {safe_type})')
            print(f'[DEBUG] [myst-block-multi] Title: {title}')
            print(f'[DEBUG] [myst-block-multi] Content snippet: {repr(content[:80])}')
            return f'<div class="admonition {safe_type}"><p class="admonition-title">{emoji} {title}</p>\n{content}</div>'
        # Match <p>:::(admonition) ...\n<p>:class: ...</p>\n(content...)<p>:::</p>
        html = re.sub(
            r'<p>:::(admonition|note|warning|tip|caution|important|error|danger|hint|check|question|quote|seealso|example|abstract|info|success|failure|bug|custom) ?([^\n<]*)</p>\n<p>:class: ([^<]*)</p>\n([\s\S]*?)<p>:::</p>',
            myst_block_multi_repl,
            html)

        # Fallback: single-paragraph MyST blocks (no <p>:class: ...</p>)
        def myst_block_single_repl(m):
            nonlocal myst_block_count
            myst_block_count += 1
            ad_type = m.group(1)
            extra = m.group(2).strip()
            content = m.group(3)
            content = re.sub(r':class:.*', '', content)
            content = content.strip()
            safe_type = re.sub(r'[^a-z0-9_-]+', '', ad_type.lower())
            emoji = get_admonition_emoji(safe_type)
            title = extra or ad_type.capitalize()
            print(f'[DEBUG] [myst-block-single] Using emoji "{emoji}" for MyST block type "{ad_type}" (class: {safe_type})')
            print(f'[DEBUG] [myst-block-single] Title: {title}')
            print(f'[DEBUG] [myst-block-single] Content snippet: {repr(content[:80])}')
            return f'<div class="admonition {safe_type}"><p class="admonition-title">{emoji} {title}</p>\n{content}</div>'
        html = re.sub(
            r'<p>:::(admonition|note|warning|tip|caution|important|error|danger|hint|check|question|quote|seealso|example|abstract|info|success|failure|bug|custom) ?([^\n<]*)</p>\n([\s\S]*?)<p>:::</p>',
            myst_block_single_repl,
            html)

        # --- Post-build checks: scan for unprocessed patterns ---
        # 1. Any remaining :class: markup
        leftover_class = re.findall(r':class:', html)
        if leftover_class:
            print(f'[CHECK] WARNING: Found {len(leftover_class)} remaining ":class:" markup in HTML output!')
        # 2. Any <p class="admonition-title"> not starting with emoji
        no_emoji_titles = re.findall(r'<p class="admonition-title">([^\s<][^<]*)</p>', html)
        for t in no_emoji_titles:
            if not re.match(r'^[^\w\s]', t):
                print(f'[CHECK] WARNING: Admonition title missing emoji: {t[:40]}')
        # 3. Any MyST/Markdown-it blocks left
        myst_left = re.findall(r'<p>:::', html)
        if myst_left:
            print(f'[CHECK] WARNING: Found {len(myst_left)} unconverted MyST blocks!')

        # Print summary of matches
        print(f'[SUMMARY] Admonition blocks processed: nbconvert-div={nbconvert_div_count}, legacy-codeblock={legacy_codeblock_count}, std-codeblock={std_codeblock_count}, myst-block={myst_block_count}')
        return html

        # 2. Convert <pre><code class="language-{admonition}">...</code></pre> blocks (legacy, fallback)
        def admonition_repl(m):
            title = m.group(1).strip()
            content = m.group(2).lstrip('\n')
            # Remove any leftover :class: markup from content
            content = re.sub(r'^:class:.*$', '', content, flags=re.MULTILINE)
            content = re.sub(r':class:.*', '', content)
            class_match = re.match(r'\s*:class:\s*([a-zA-Z0-9_-]+)\s*\n(.*)', content, re.DOTALL)
            if class_match:
                ad_class = class_match.group(1).strip()
                content = class_match.group(2).lstrip('\n')
            else:
                ad_class = ''
            safe_title = re.sub(r'[^a-z0-9_-]+', '', title.lower().replace(' ', '-'))
            class_attr = f'admonition {ad_class}' if ad_class else f'admonition {safe_title}'
            emoji = get_admonition_emoji(ad_class or safe_title)
            print(f'[DEBUG] Using emoji "{emoji}" for title "{title}" (class: {ad_class or safe_title})')
            title_html = f'<p class="admonition-title">{emoji} {title}</p>'
            return f'<div class="{class_attr}">{title_html}\n{content.strip()}</div>'
        html = re.sub(
            r'<pre><code class="language-\{admonition\}">\{admonition\}\s*([^\n]*)\n([\s\S]*?)</code></pre>',
            admonition_repl,
            html)

        # 3. Convert <pre><code class="language-{type}">{type} ...</code></pre> blocks (note, warning, tip, etc)
        def std_admonition_repl(m):
            ad_type = m.group(1)
            extra = m.group(2).strip()
            content = m.group(3).strip()
            emoji = get_admonition_emoji(ad_type)
            print(f'[DEBUG] Using emoji "{emoji}" for standard admonition type "{ad_type}"')
            title = f"{ad_type.capitalize()} {extra}".strip()
            return f'<div class="admonition {ad_type}"><p class="admonition-title">{emoji} {title}</p>\n{content}</div>'
        html = re.sub(
            r'<pre><code class="language-\{(note|warning|tip|caution|important|error|danger|hint|check|question|quote|seealso|example|abstract|info|success|failure|bug|custom)\}">\{\1\}([^\n]*)\n([\s\S]*?)</code></pre>',
            std_admonition_repl,
            html)

        # 4. Convert ::: blocks (MyST/Markdown-it style)
        def myst_block_repl(m):
            ad_type = m.group(1)
            extra = m.group(2).strip()
            content = m.group(3).strip()
            safe_type = re.sub(r'[^a-z0-9_-]+', '', ad_type.lower())
            emoji = get_admonition_emoji(safe_type)
            print(f'[DEBUG] Using emoji "{emoji}" for MyST block type "{ad_type}" (class: {safe_type})')
            title = extra or ad_type.capitalize()
            return f'<div class="admonition {safe_type}"><p class="admonition-title">{emoji} {title}</p>\n{content}</div>'
        html = re.sub(
            r'<p>:::(admonition|note|warning|tip|caution|important|error|danger|hint|check|question|quote|seealso|example|abstract|info|success|failure|bug|custom) ?([^\n<]*)</p>\n([\s\S]*?)<p>:::</p>',
            myst_block_repl,
            html)
        return html



    # --- Define and initialize missing globals for post-main() code ---

# Only create folders and run main() if run as script
# (Removed duplicate/empty post_build_cleanup and misplaced imports)

def post_build_cleanup():
    images_dir = build_dir / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)
    images_root_candidates = [repo_root / 'content' / 'images', notebooks_dir / 'images']
    all_section_image_map = {}
    all_missing_images = set()
    all_youtube_ids = set()
    def ensure_section_dir(section):
        d = images_dir / section.lower()
        d.mkdir(parents=True, exist_ok=True)
        return d
    def path_to_output_name(name, section):
        return f"{section.lower()}/{name}"

    # --- Build menu_html_names mapping: html_name -> section ---
    menu_html_names = {}
    import json, yaml, re
    menu_yml = repo_root / '_menu.yml'
    menu_data = None
    if menu_yml.exists():
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
            def walk_menu(items, section=None):
                for item in items:
                    title = item.get('title', '')
                    path = item.get('path', None)
                    if path and path.endswith('.html'):
                        menu_html_names[path] = section or title or 'other'
                    if 'children' in item:
                        walk_menu(item['children'], title)
            walk_menu(menu_data)
        except Exception as e:
            print(f'[ERROR] Could not build menu_html_names: {e}')

    # --- Aggregate missing images and YouTube thumbnails across all notebooks listed in _notebooks.yaml ---
    notebooks_yaml = repo_root / '_notebooks.yaml'
    nb_list = []
    if notebooks_yaml.exists():
        try:
            with open(notebooks_yaml, 'r') as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict) and 'notebooks' in data:
                nb_list = data['notebooks']
            elif isinstance(data, list):
                nb_list = data
            else:
                print("[ERROR] _notebooks.yaml format not recognized.")
        except Exception as e:
            print(f"[ERROR] Failed to read _notebooks.yaml: {e}")
    # nb_list is now always a list, even if empty or error

    for nb in nb_list:
        nb_path = Path(nb)
        if not nb_path.is_absolute():
            nb_path = repo_root / nb_path
        nb_path = nb_path.resolve()
        html_name = nb_path.with_suffix('.html').name
        section = menu_html_names.get(html_name, 'other')
        all_section_image_map[html_name] = section
        section_dir = ensure_section_dir(section)
        if not nb_path.exists():
            print(f"[WARNING] Notebook not found: {nb_path}")
            continue
        nb_data = nbformat.read(str(nb_path), as_version=4)
        referenced_images = set()
        for cell in nb_data.cells:
            if cell.cell_type != 'markdown':
                continue
            def update_img_link(m):
                alt_text = m.group(1)
                img_path = m.group(2).strip()
                # --- YOUTUBE THUMBNAIL HANDLING ---
                yt_match = re.match(r'https?://img.youtube.com/vi/([\w-]{11})/', img_path)
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
                        if images_root.exists() and images_root.is_dir():
                            for section_dir in images_root.iterdir():
                                if section_dir.is_dir():
                                    candidate = section_dir / os.path.basename(clean_name)
                                    if candidate.exists():
                                        real_img_path = candidate
                                        found = True
                                        break
                            if found:
                                break
                    # else: skip this images_root if it doesn't exist
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


    # 4. Convert notebooks to HTML with custom CSS and template
    import json
    css_light_path = repo_root / 'static' / 'css' / 'theme-light.css'
    css_dark_path = repo_root / 'static' / 'css' / 'theme-dark.css'
    css_light_rel = 'css/theme-light.css'
    css_dark_rel = 'css/theme-dark.css'

    # --- Load menu structure from _menu.yml using basic_yaml2json.py ---
    menu_yml = repo_root / '_menu.yml'
    menu_data = None
    if menu_yml.exists():
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
            html += '<ul class="site-nav-menu" id="site-nav-menu">'
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
        nav_html = ''
        # nav_html = '<button class="site-nav-toggle" aria-label="Open menu" aria-controls="site-nav-menu" aria-expanded="false" tabindex="0">☰</button>'  # Hamburger menu commented out
        # Use menu_data if available, else fallback
        if menu_data:
            nav_html += build_menu_html(menu_data)
        else:
            nav_html += '<!-- Menu data not available, fallback menu here -->'
        # Removed dark mode toggle button
        nav_html += """
<!-- Hamburger menu and toggle JS commented out -->
"""
        return nav_html

    def get_html_template(title, body):
        nav_html = get_nav_html()
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
        # Read the HTML template from static/html_template.html
        template_path = Path(__file__).parent / 'static/html_template.html'
        if not template_path.exists():
            raise FileNotFoundError(f"HTML template not found: {template_path}")
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        # Replace placeholders
        html = template.format(title=book_title, body=body, nav=nav_html, footer=footer_html)
        return html

    # --- Process index.md and cards.md as index.html ---
    index_md = repo_root / 'content/index.md'
    cards_md = repo_root / 'content/cards.md'
    announcement_md = repo_root / 'content/announcement.md'
    index_html_path = build_dir / 'index.html'
    title = 'Modern Classical Mechanics'
    main_html = ''
    card_grid = ''
    announcement_html = ''
    if announcement_md.exists():
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(announcement_md, 'r', encoding='utf-8') as f:
            announcement_content = f.read()
        # Wrap in .wip-banner div for styling and accessibility
        announcement_html = f'<div class="wip-banner" role="status" aria-label="Announcement">' + markdown.markdown(announcement_content, extensions=['extra', 'admonition']) + '</div>'
    if index_md.exists():
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(index_md, 'r', encoding='utf-8') as f:
            index_content = f.read()
        # Optionally extract title from first heading
        m = re.match(r'^# (.+)', index_content)
        if m:
            title = m.group(1).strip()
        main_html = markdown.markdown(index_content, extensions=['extra', 'toc', 'admonition'])
        # Prepend announcement if present
        if announcement_html:
            main_html = announcement_html + main_html
    # --- Build homepage card grid from _menu.yml, with optional Markdown overrides ---
    card_grid = ''
    if menu_data:
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        # Parse cards.md into sections (split by headings)
        card_md_sections = {}
        if cards_md.exists():
            with open(cards_md, 'r', encoding='utf-8') as f:
                cards_content = f.read()
            # Split on headings (### ...)
            for m in re.finditer(r'^### +(.+?)\n([\s\S]*?)(?=^### |\Z)', cards_content, re.MULTILINE):
                sec_title = m.group(1).strip()
                sec_body = m.group(2).strip()
                card_md_sections[sec_title.lower()] = sec_body
        card_grid = '<section class="card-grid" aria-label="Main sections">'
        for item in menu_data:
            title = item.get('title', '').strip()
            # Exclude "Home" from card grid
            if title.lower() == 'home':
                continue
            path = item.get('path', None)
            desc = item.get('description', '').strip() if 'description' in item else ''
            # Use Markdown override if present
            md_body = card_md_sections.get(title.lower(), '').strip()
            card_body = md_body if md_body else desc
            card_title = title  # Use the section heading as the card title
            card_body_md = card_body.strip()
            # Remove any --- lines (horizontal rules) from the card body before rendering
            card_body_md_clean = '\n'.join(line for line in card_body_md.split('\n') if line.strip() != '---')
            card_body_html = markdown.markdown(card_body_md_clean, extensions=['extra', 'admonition']) if card_body_md_clean else ''
            card_id = f"card-{title.lower().replace(' ', '-')}"
            if path:
                card_grid += (
                    f'<a class="download-btn card-home-btn" href="{path}" role="button" tabindex="0" aria-labelledby="{card_id}">' # Use .download-btn for homepage cards
                    f'<span class="card-home-btn-inner">'
                    f'<h2 id="{card_id}">{card_title}</h2>'
                    f'{card_body_html}'
                    f'</span></a>'
                )
            else:
                card_grid += (
                    f'<span class="download-btn card-home-btn" role="button" tabindex="0" aria-labelledby="{card_id}">' # Non-link fallback
                    f'<span class="card-home-btn-inner">'
                    f'<h2 id="{card_id}">{card_title}</h2>'
                    f'{card_body_html}'
                    f'</span></span>'
                )
        card_grid += '</section>'
    if main_html:
        body = f'<div class="markdown-body">{main_html}{card_grid}</div>'
        html = get_html_template(title, body)
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
            # Improved: Scan the chapter HTML for the first <img> tag and use that as the thumbnail if found
            thumb_img = None
            thumb_alt = title
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
            # Fallback: Try to find an image matching the chapter file name in images/chapters
            if not thumb_img:
                section_img_dir = docs_dir / 'images' / section
                base_name = Path(path).stem
                if section_img_dir.exists():
                    for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                        candidate = section_img_dir / f"{base_name}{ext}"
                        if candidate.exists():
                            thumb_img = f'images/{section}/{candidate.name}'
                            break
            # Fallback: Use the first image in the section folder
            if not thumb_img:
                section_img_dir = docs_dir / 'images' / section
                if section_img_dir.exists():
                    for f in sorted(section_img_dir.iterdir()):
                        if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg'] and not f.name.startswith('.._.._'):
                            thumb_img = f'images/{section}/{f.name}'
                            break
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

    # --- Build resources.html from resources.md ---
    resources_md = repo_root / 'content/resources.md'
    resources_html_path = build_dir / 'resources.html'
    if resources_md.exists():
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(resources_md, 'r', encoding='utf-8') as f:
            resources_content = f.read()
        resources_html = markdown.markdown(resources_content, extensions=['extra', 'toc', 'admonition'])
        body = f'<div class="markdown-body">{resources_html}</div>'
        html = get_html_template("Resources", body)
        with open(resources_html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # --- Build about.html from about.md ---
    about_md = repo_root / 'content/about.md'
    about_html_path = build_dir / 'about.html'
    if about_md.exists():
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(about_md, 'r', encoding='utf-8') as f:
            about_content = f.read()
        about_html = markdown.markdown(about_content, extensions=['extra', 'toc', 'admonition'])
        body = f'<div class="markdown-body">{about_html}</div>'
        html = get_html_template("About", body)
        with open(about_html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # --- Build activities.html from activities.md ---
    activities_md = repo_root / 'content/activities.md'
    activities_html_path = build_dir / 'activities.html'
    if activities_md.exists():
        try:
            import markdown
        except ImportError:
            print("[ERROR] The 'markdown' package is required. Install it with 'pip install markdown'.")
            sys.exit(1)
        with open(activities_md, 'r', encoding='utf-8') as f:
            activities_content = f.read()
        activities_html = markdown.markdown(activities_content, extensions=['extra', 'toc', 'admonition'])
        body = f'<div class="markdown-body">{activities_html}</div>'
        html = get_html_template("Activities", body)
        with open(activities_html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    # --- Process all notebooks as HTML with the same template, rewriting image links to section subfolders ---
    # Build a mapping from all copied images: filename -> (section, relpath)
    copied_images = {}
    for section_dir in images_dir.iterdir():
        if section_dir.is_dir():
            section = section_dir.name
            for img_file in section_dir.iterdir():
                if img_file.is_file():
                    copied_images[img_file.name] = (section, f'images/{section}/{img_file.name}')

    for nb in nb_list:
        nb_path = Path(nb)
        if not nb_path.is_absolute():
            nb_path = repo_root / nb_path
        nb_path = nb_path.resolve()
        html_name = nb_path.with_suffix('.html').name
        section = menu_html_names.get(html_name, 'other')
        html_path = build_dir / html_name
        # --- Preprocess notebook for custom admonitions ---
        import tempfile
        changed = False
        if not nb_path.exists():
            print(f"[WARNING] Notebook not found: {nb_path}")
            continue
        nb_data = nbformat.read(str(nb_path), as_version=4)
        for i, cell in enumerate(nb_data.cells):
            if cell.cell_type == 'markdown':
                orig_source = cell.source
                # Robustly replace MyST-style code fences for custom admonitions
                def myst_admonition_repl(match):
                    title = match.group(1).strip()
                    body = match.group(2).strip()
                    safe_title = re.sub(r'[^a-z0-9_-]+', '', title.lower().replace(' ', '-'))
                    html = f'<div class="admonition {safe_title}"><p class="admonition-title">{title}</p>\n{body}</div>'
                    print(f"[PREPROCESS] Rewriting MyST admonition in cell {i+1}: title='{title}'")
                    return html
                # Handles ```{admonition} Title\nBody\n```
                new_source = re.sub(
                    r'```\{admonition\}\s*([^\n]+)\n([\s\S]*?)```',
                    myst_admonition_repl,
                    orig_source,
                    flags=re.MULTILINE
                )
                # Also handle indented code blocks (rare)
                if new_source == orig_source:
                    new_source2 = re.sub(
                        r'^\s*\{admonition\}\s+([^\n]+)\n([\s\S]*?)(?=\n\n|\Z)',
                        lambda m: myst_admonition_repl(m),
                        orig_source,
                        flags=re.MULTILINE
                    )
                    if new_source2 != orig_source:
                        print(f"[PREPROCESS] (Indented) Cell {i+1} changed.")
                        new_source = new_source2
                if new_source != orig_source:
                    print(f"[PREPROCESS] Cell {i+1} changed.")
                    cell.source = new_source
                    changed = True
        if changed:
            with tempfile.NamedTemporaryFile('w', suffix='.ipynb', delete=False) as tf:
                nbformat.write(nb_data, tf)
                temp_nb_path = tf.name
            print(f"[PREPROCESS] Using temp notebook: {temp_nb_path}")
            nb_to_convert = temp_nb_path
        else:
            nb_to_convert = str(nb)

        exporter = HTMLExporter()
        (body, resources) = exporter.from_filename(nb_to_convert)

        if changed:
            try:
                os.unlink(temp_nb_path)
                print(f"[PREPROCESS] Deleted temp notebook: {temp_nb_path}")
            except Exception as e:
                print(f"[PREPROCESS] Could not delete temp notebook: {temp_nb_path} ({e})")

        # Extract only the <body>...</body> content if present
        import re
        m = re.search(r'<body[^>]*>([\s\S]*?)</body>', body, re.IGNORECASE)
        if m:
            body_content = m.group(1)
        else:
            body_content = body

        def rewrite_img_src(match):
            src = match.group(1)
            filename = os.path.basename(src)
            if filename in copied_images:
                new_section, new_rel = copied_images[filename]
                return f'src="{new_rel}"'
            return match.group(0)
        body_content = re.sub(r'src=["\']([^"\']+)["\']', rewrite_img_src, body_content)

        # Ensure these helpers are available (move to top-level if needed)
        if 'preprocess_custom_admonitions' not in globals():
            def preprocess_custom_admonitions(x): return x
        if 'convert_admonitions' not in globals():
            def convert_admonitions(x): return x
        body_content = preprocess_custom_admonitions(body_content)
        body_content = convert_admonitions(body_content)

        chapter_stem = nb_path.stem
        # --- Set Jupyter HTML link to match actual output location ---
        jupyter_link = f'jupyter/content/notebooks/{chapter_stem}.html'
        download_menu = f'''
<nav class="chapter-downloads" aria-label="Download chapter sources">
  <div role="group" aria-label="Download formats">
    <a class="download-btn" href="sources/{chapter_stem}/{chapter_stem}.pdf" download><span aria-hidden="true">📄</span> PDF</a>
    <a class="download-btn" href="sources/{chapter_stem}/{chapter_stem}.docx" download><span aria-hidden="true">📝</span> DOCX</a>
    <a class="download-btn" href="sources/{chapter_stem}/{chapter_stem}.md" download><span aria-hidden="true">✍️</span> MD</a>
    <a class="download-btn" href="sources/{chapter_stem}/{chapter_stem}.ipynb" download><span aria-hidden="true">📓</span> IPYNB</a>
    <a class="download-btn" href="sources/{chapter_stem}/{chapter_stem}.tex" download><span aria-hidden="true">📐</span> TEX</a>
    <a class="download-btn" href="{jupyter_link}" target="_blank"><span aria-hidden="true">🔗</span> Jupyter</a>
  </div>
</nav>
        '''
        body_final = f'{download_menu}<div class="markdown-body">{body_content}</div>'
        title = nb_path.stem.replace('_', ' ').title()
        html = get_html_template(title, body_final)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)


    # 5. Copy everything to docs/ and move source files for download links

    docs_css_dir = docs_dir / 'css'
    docs_css_dir.mkdir(parents=True, exist_ok=True)
    # Clean docs/ except .nojekyll
    for item in docs_dir.iterdir():
        if item.name == '.nojekyll':
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    # Copy HTML build output to docs/
    for item in build_dir.iterdir():
        dest = docs_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    # Copy theme-light.css and theme-dark.css to docs/css and _build/html/css
    docs_css_dir.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(css_light_path, docs_css_dir / 'theme-light.css')
        shutil.copy2(css_dark_path, docs_css_dir / 'theme-dark.css')
    except Exception as e:
        print(f"[ERROR] Failed to copy theme CSS to {docs_css_dir}: {e}")
        raise
    build_css_dir = build_dir / 'css'
    build_css_dir.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(css_light_path, build_css_dir / 'theme-light.css')
        shutil.copy2(css_dark_path, build_css_dir / 'theme-dark.css')
    except Exception as e:
        print(f"[ERROR] Failed to copy theme CSS to {build_css_dir}: {e}")
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

    # --- Copy all source files for download links ---
    # For each notebook, copy .pdf, .docx, .md, .ipynb, .tex to docs/sources/<notebook>/<notebook>.<ext>
    sources_dir = docs_dir / 'sources'
    sources_dir.mkdir(parents=True, exist_ok=True)
    # List of all notebook stems (without extension), including all chapters and activities (anything in _notebooks.yaml)
    # Use _notebooks.yaml as authoritative list
    import yaml
    notebooks_yaml = repo_root / '_notebooks.yaml'
    notebook_stems = set()
    if notebooks_yaml.exists():
        with open(notebooks_yaml, 'r') as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and 'notebooks' in data:
                for nb in data['notebooks']:
                    stem = Path(nb).with_suffix('').name
                    notebook_stems.add(stem)
    # Fallback: add any .ipynb in notebooks/ not already listed
    for nb in notebooks_dir.glob('*.ipynb'):
        stem = nb.with_suffix('').name
        notebook_stems.add(stem)
    notebook_stems = sorted(notebook_stems)
    # Map of output extensions and their build locations
    output_exts = {
        'pdf': repo_root / '_build' / 'pdf',
        'docx': repo_root / '_build' / 'docx',
        'md': repo_root / '_build' / 'md',
        'ipynb': notebooks_dir,
        'tex': repo_root / '_build' / 'latex',
    }
    for stem in notebook_stems:
        chapter_dir = sources_dir / stem
        chapter_dir.mkdir(parents=True, exist_ok=True)
        for ext, src_dir in output_exts.items():
            src_file = src_dir / f"{stem}.{ext}"
            dest_file = chapter_dir / f"{stem}.{ext}"
            if src_file.exists():
                shutil.copy2(src_file, dest_file)

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

    print("All notebooks converted to HTML and copied to docs/ with sectioned images, CSS, accessible menu, and downloadable sources.")

    # --- AUTOMATE: Copy all images from HTML build output to LaTeX images dir if referenced in LaTeX but missing ---
    latex_images_dir = repo_root / '_build' / 'latex' / 'images'
    html_images_dir = repo_root / '_build' / 'html' / 'images'
    latex_dir = repo_root / '_build' / 'latex'
    latex_images_dir.mkdir(parents=True, exist_ok=True)
    # Find all .tex files in _build/latex
    import glob
    tex_files = list(latex_dir.glob('*.tex'))
    import re
    for tex_file in tex_files:
        with open(tex_file, 'r', encoding='utf-8') as f:
            tex_content = f.read()
        # Find all \includegraphics{...} usages
        img_refs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^\}]+)\}', tex_content)
        for img_ref in img_refs:
            img_name = os.path.basename(img_ref)
            dest_img = latex_images_dir / img_name
            if not dest_img.exists():
                # Try to copy from HTML build images dir (flat and sectioned)
                src_candidates = [html_images_dir / img_name]
                # Also try all subfolders (sectioned)
                src_candidates += [p for p in html_images_dir.glob('**/' + img_name)]
                copied = False
                for src in src_candidates:
                    if src.exists():
                        try:
                            shutil.copy2(src, dest_img)
                            print(f"[AUTO-COPY] Copied missing LaTeX image: {img_name} from {src} to {dest_img}")
                            copied = True
                            break
                        except Exception as e:
                            print(f"[AUTO-COPY][ERROR] Could not copy {src} to {dest_img}: {e}")
                if not copied:
                    print(f"[AUTO-COPY][WARN] Could not find image {img_name} for LaTeX in HTML build images.")

    # Always clean docs/ HTML after build
    # Ensure this helper is available at top-level
    if 'clean_html_files_in_docs' not in globals():
        def clean_html_files_in_docs():
            pass
    clean_html_files_in_docs()

if __name__ == '__main__':
    main()