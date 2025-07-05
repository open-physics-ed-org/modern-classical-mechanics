import sys
from bs4 import BeautifulSoup
import re

# Files to check
files = [
    "docs/index.html",
    "_build/html/index.html"
]

css_file = "docs/css/main.css"

# Helper to extract CSS rules for a selector inside a media query

def extract_mobile_css(css, selector):
    # Find the mobile media query
    m = re.search(r'@media[^{]*\(max-width: ?900px\)[^{]*{(.*?)}\s*}', css, re.DOTALL)
    if not m:
        return None
    block = m.group(1)
    # Find the selector block
    sel = re.search(r'(' + re.escape(selector) + r'\s*{[^}]*})', block)
    return sel.group(1) if sel else None

def check_nav_ul_display(css):
    # Check for .site-nav ul in mobile media query
    mobile_ul = extract_mobile_css(css, '.site-nav ul')
    if not mobile_ul:
        print("FAIL: No .site-nav ul block in mobile media query")
        return False
    # Check display property
    display = re.search(r'display\s*:\s*([^;]+);', mobile_ul)
    if not display:
        print("FAIL: No display property for .site-nav ul in mobile")
        return False
    value = display.group(1).strip()
    if value not in ("flex", "block", "inline-flex"):
        print(f"FAIL: .site-nav ul display on mobile is '{value}', should be 'flex' or 'block'")
        return False
    print(f"PASS: .site-nav ul display on mobile is '{value}'")
    return True

def check_nav_visible_in_html(file):
    with open(file) as f:
        soup = BeautifulSoup(f, "html.parser")
    nav = soup.find("nav", class_="site-nav")
    if not nav:
        print(f"FAIL: No <nav class='site-nav'> in {file}")
        return False
    ul = nav.find("ul")
    if not ul:
        print(f"FAIL: No <ul> in nav in {file}")
        return False
    print(f"PASS: <nav class='site-nav'><ul> present in {file}")
    return True

def main():
    print("Checking mobile nav CSS visibility...")
    with open(css_file) as f:
        css = f.read()
    css_ok = check_nav_ul_display(css)
    print("\nChecking nav HTML in outputs...")
    html_ok = all(check_nav_visible_in_html(f) for f in files)
    if css_ok and html_ok:
        print("\nPASS: Mobile nav should be visible and present.")
        sys.exit(0)
    else:
        print("\nFAIL: Mobile nav visibility or structure is broken.")
        sys.exit(1)

if __name__ == "__main__":
    main()
