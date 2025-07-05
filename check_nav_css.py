import sys
from pathlib import Path

# Files to check
FILES = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]

# CSS selectors and color variables to check for (UPDATED FOR MODERN NAV)
CSS_CHECKS = [
    ('.site-nav-menu', 'display:'),
    ('.dropdown-menu', 'display:'),
    (':root', '--color-bg:'),
]

LEGACY_SELECTORS = [
    'menu-toggle', # still flag legacy hamburger if present
    'side-nav',
    'side-menu',
    '☰',
]

def check_css_link(html):
    """Check if main.css is linked in the HTML."""
    return 'css/main.css' in html


def check_css_vars(html, css_path='docs/css/main.css'):
    """Check if color variables and nav CSS are present in a <style> block (inlined) or loaded from main.css."""
    # Check for variables and nav in HTML (inlined)
    has_vars_html = '--color-bg:' in html or 'var(--color-bg)' in html
    has_nav_html = (
        '.site-nav' in html or
        'class="site-nav"' in html or
        'class=\'site-nav\'' in html
    )
    # Check for variables and nav in linked CSS file
    css_ok = False
    try:
        css = Path(css_path).read_text(errors='replace')
        css_ok = '--color-bg:' in css and '.site-nav' in css
    except Exception:
        pass
    return (has_vars_html and has_nav_html) or css_ok

def check_legacy(html):
    """Check for legacy nav elements."""
    found = []
    for sel in LEGACY_SELECTORS:
        if sel in html:
            found.append(sel)
    return found

def main():
    all_passed = True
    for file in FILES:
        if not file.exists():
            print(f'FAIL: {file} does not exist')
            all_passed = False
            continue
        html = file.read_text(encoding='utf-8')
        print(f'Checking {file}...')
        # Check CSS link
        if not check_css_link(html):
            print('  FAIL: main.css is not linked!')
            all_passed = False
        else:
            print('  PASS: main.css is linked')
        # Check CSS variables and nav CSS
        if not check_css_vars(html):
            print('  FAIL: CSS variables or nav CSS missing!')
            all_passed = False
        else:
            print('  PASS: CSS variables and nav CSS found')
        # Check for legacy nav
        legacy = check_legacy(html)
        if legacy:
            print(f'  FAIL: Legacy nav elements found: {legacy}')
            all_passed = False
        else:
            print('  PASS: No legacy nav elements found')
    if all_passed:
        print('\nALL CHECKS PASSED: main.css is used and no legacy nav remains.')
        sys.exit(0)
    else:
        print('\nCHECKS FAILED: See above for details.')
        sys.exit(1)

if __name__ == '__main__':
    main()
