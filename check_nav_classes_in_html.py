"""
Check that all nav-related classes used in the CSS are present in the HTML output.
This is the inverse of the CSS check: it finds all nav classes in main.css and checks for their use in docs/*.html.
"""
import re
from pathlib import Path

CSS_PATH = Path('docs/css/main.css')
HTML_PATHS = list(Path('docs').glob('*.html'))

# Find all nav-related classes in CSS
NAV_CLASS_PATTERN = re.compile(r'\.([\w-]*nav[\w-]*)\b')
css_text = CSS_PATH.read_text(encoding='utf-8')
css_classes = set(NAV_CLASS_PATTERN.findall(css_text))

missing = []
for cls in css_classes:
    found = False
    for html_path in HTML_PATHS:
        html = html_path.read_text(encoding='utf-8')
        if f'class="{cls}"' in html or f'class=\'{cls}\'' in html:
            found = True
            break
    if not found:
        missing.append(cls)

if missing:
    print(f"FAIL: These nav-related classes are in main.css but not used in any HTML: {', '.join(missing)}")
else:
    print("PASS: All nav-related classes in main.css are used in HTML output.")
