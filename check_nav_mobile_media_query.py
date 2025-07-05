"""
Check that .site-nav-menu and .dropdown-menu have display rules inside the mobile media query in main.css.
"""
import re
from pathlib import Path

CSS_PATH = Path('docs/css/main.css')
NAV_CLASSES = ['site-nav-menu', 'dropdown-menu']
MEDIA_QUERY_PATTERN = re.compile(r'@media\s*\(max-width:\s*900px\)[^{]*{([^}]*)}', re.DOTALL)

css = CSS_PATH.read_text(encoding='utf-8')
media_blocks = MEDIA_QUERY_PATTERN.findall(css)

for cls in NAV_CLASSES:
    found = False
    for block in media_blocks:
        if f'.{cls}' in block:
            found = True
            print(f"PASS: .{cls} has rules in mobile media query.")
            break
    if not found:
        print(f"FAIL: .{cls} missing from mobile media query.")
