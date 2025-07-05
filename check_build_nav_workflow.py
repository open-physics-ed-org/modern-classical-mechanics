#!/usr/bin/env python3
"""
check_build_nav_workflow.py
Comprehensive workflow checker for navigation build/debug:
- Checks for nav HTML, nav CSS, and nav visibility in both docs/ and _build/html/ outputs
- Checks for presence and content of main.css in both locations
- Checks for override <style> blocks that may break nav
- Checks for legacy/mobile nav remnants in HTML and CSS
- Checks for JS that might affect nav
- Reports summary and actionable diagnostics
"""
import re
from pathlib import Path

# Paths
css_paths = [Path('docs/css/main.css'), Path('_build/html/css/main.css')]
html_paths = [Path('docs/index.html'), Path('_build/html/index.html')]

# Checks
NAV_CLASSES = ['site-nav', 'site-nav-menu', 'dropdown-menu']
LEGACY_CLASSES = ['menu-toggle', 'side-nav', 'side-menu']
OVERRIDE_STYLE_ID = 'site-bg-override'


def check_file_exists(path):
    return path.exists()

def check_css_contains(path, selectors):
    if not path.exists():
        return False, []
    css = path.read_text(errors='replace')
    found = [s for s in selectors if s in css]
    return bool(found), found

def check_html_nav(html):
    # Look for nav HTML structure
    nav = re.search(r'<nav[^>]*class="[^"]*site-nav[^"]*"', html)
    menu = re.search(r'class="[^"]*site-nav-menu[^"]*"', html)
    dropdown = re.search(r'class="[^"]*dropdown-menu[^"]*"', html)
    return bool(nav and menu and dropdown)

def check_html_override_style(html):
    return f'id="{OVERRIDE_STYLE_ID}"' in html

def check_html_legacy(html):
    found = [c for c in LEGACY_CLASSES if c in html]
    return found

def check_css_legacy(css):
    found = [c for c in LEGACY_CLASSES if c in css]
    return found

def check_js_nav(html):
    # Look for nav-related JS (inline or linked)
    js = re.findall(r'<script[^>]+src=["\"][^>]+\.js["\"][^>]*>', html)
    inline = re.findall(r'<script[^>]*>.*?(menu|nav)', html, re.DOTALL|re.IGNORECASE)
    return js, inline

def main():
    print('--- NAV BUILD WORKFLOW CHECK ---')
    # CSS checks
    for css_path in css_paths:
        print(f'Checking {css_path}...')
        if not check_file_exists(css_path):
            print('  FAIL: File missing!')
            continue
        ok, found = check_css_contains(css_path, NAV_CLASSES)
        if ok:
            print(f'  PASS: Found nav classes: {found}')
        else:
            print('  FAIL: Nav classes missing!')
        legacy = check_css_legacy(css_path.read_text(errors="replace"))
        if legacy:
            print(f'  WARNING: Legacy/mobile nav CSS present: {legacy}')
        else:
            print('  PASS: No legacy/mobile nav CSS')
    # HTML checks
    for html_path in html_paths:
        print(f'Checking {html_path}...')
        if not check_file_exists(html_path):
            print('  FAIL: File missing!')
            continue
        html = html_path.read_text(errors='replace')
        if check_html_nav(html):
            print('  PASS: Nav HTML structure present')
        else:
            print('  FAIL: Nav HTML structure missing or broken!')
        if check_html_override_style(html):
            print(f'  WARNING: Override style block (id={OVERRIDE_STYLE_ID}) present!')
        else:
            print('  PASS: No override style block')
        legacy = check_html_legacy(html)
        if legacy:
            print(f'  WARNING: Legacy/mobile nav HTML present: {legacy}')
        else:
            print('  PASS: No legacy/mobile nav HTML')
        js, inline = check_js_nav(html)
        if js or inline:
            print(f'  INFO: Nav-related JS found: {js + inline}')
        else:
            print('  PASS: No nav-related JS found')
    print('--- END OF CHECK ---')

if __name__ == '__main__':
    main()
