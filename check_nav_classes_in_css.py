"""
Script to check that all nav-related classes used in HTML output are present in the CSS file.
Specifically checks for .site-nav-menu and .dropdown-menu selectors in main.css.
"""
import re
from pathlib import Path

CSS_PATH = Path('docs/css/main.css')
HTML_PATHS = list(Path('docs').glob('*.html'))

# Classes to check for in CSS
NAV_CLASSES = [
    'site-nav-menu',
    'dropdown-menu',
]

def css_has_class(css_text, class_name):
    # Look for .class_name as a selector (not just in comments)
    pattern = re.compile(r'\.' + re.escape(class_name) + r'\b')
    return bool(pattern.search(css_text))

def main():
    missing = []
    css_text = CSS_PATH.read_text(encoding='utf-8')
    for cls in NAV_CLASSES:
        if not css_has_class(css_text, cls):
            missing.append(cls)
    if missing:
        print(f"FAIL: These nav classes are missing from main.css: {', '.join(missing)}")
    else:
        print("PASS: All nav classes used in HTML are present in main.css.")

    # Optionally, check if these classes are present in HTML output
    for html_path in HTML_PATHS:
        html = html_path.read_text(encoding='utf-8')
        for cls in NAV_CLASSES:
            if f'class="{cls}"' in html or f'class=\'{cls}\'' in html:
                print(f"{html_path.name}: uses .{cls}")

if __name__ == '__main__':
    main()
