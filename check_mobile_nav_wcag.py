#!/usr/bin/env python3
"""
check_mobile_nav_wcag.py
Checks for presence and WCAG compliance of mobile navigation in built HTML and CSS.
Verifies ARIA attributes, keyboard accessibility, and correct CSS for <=760px.
"""
import re
from pathlib import Path

css_file = Path('docs/css/main.css')
outputs = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]

# Check for mobile nav CSS (media query)
css = css_file.read_text(errors='replace') if css_file.exists() else ''
if '@media (max-width: 760px)' not in css:
    print('ERROR: No mobile nav media query for <=760px in main.css!')
else:
    print('Mobile nav media query found in main.css.')

# Check for nav toggle button and ARIA attributes in HTML
for out in outputs:
    print(f'Checking {out} for mobile nav and ARIA...')
    if not out.exists():
        print('  File not found.')
        continue
    html = out.read_text(errors='replace')
    # Look for nav toggle button
    if not re.search(r'<button[^>]*class=["\"][^"\"]*site-nav-toggle', html):
        print('  ERROR: No .site-nav-toggle button found!')
    else:
        print('  .site-nav-toggle button found.')
    # Check ARIA attributes
    if not re.search(r'aria-controls=["\"][^"\"]*site-nav-menu', html):
        print('  ERROR: No aria-controls for nav menu!')
    if not re.search(r'aria-expanded', html):
        print('  ERROR: No aria-expanded attribute on nav toggle!')
    if not re.search(r'role=["\"]menubar["\"]', html):
        print('  ERROR: No role="menubar" on nav!')
    if not re.search(r'role=["\"]menuitem["\"]', html):
        print('  ERROR: No role="menuitem" on nav items!')
    # Check for keyboard accessibility (tabindex)
    if not re.search(r'tabindex=["\"]0["\"]', html):
        print('  WARNING: No tabindex="0" found for nav items (should be present for keyboard nav)!')
print('Done.')
