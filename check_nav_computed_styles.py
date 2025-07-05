"""
Check computed styles for nav elements in built HTML using BeautifulSoup and a simple CSS parser.
Reports if .site-nav-menu and .dropdown-menu are set to display:none or not visible by default.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re

CSS_PATH = Path('docs/css/main.css')
HTML_PATHS = list(Path('docs').glob('*.html'))

# Parse CSS for display property of nav classes
NAV_CLASSES = ['site-nav-menu', 'dropdown-menu']

def get_display_for_class(css, class_name):
    # Find the last display property for .class_name
    pattern = re.compile(r'\.' + re.escape(class_name) + r'\b[^}]*{[^}]*display\s*:\s*([^;]+);', re.MULTILINE)
    matches = pattern.findall(css)
    return matches[-1].strip() if matches else None

def main():
    css = CSS_PATH.read_text(encoding='utf-8')
    for cls in NAV_CLASSES:
        display = get_display_for_class(css, cls)
        if display is None:
            print(f"FAIL: No display property found for .{cls} in main.css")
        else:
            print(f". {cls}: display = {display}")
    # Check if nav elements are present in HTML
    for html_path in HTML_PATHS:
        soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
        for cls in NAV_CLASSES:
            if soup.find(class_=cls):
                print(f"{html_path.name}: .{cls} found")
            else:
                print(f"{html_path.name}: .{cls} NOT found")

if __name__ == '__main__':
    main()
