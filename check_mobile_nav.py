import sys
from bs4 import BeautifulSoup

# Files to check
files = [
    "docs/index.html",
    "_build/html/index.html"
]

# CSS file to check
css_file = "docs/css/main.css"

# Check for .site-nav and .site-nav ul always visible on mobile
MOBILE_MEDIA_QUERY = "@media (max-width: 900px)"
MOBILE_SITE_NAV = ".site-nav {"
MOBILE_SITE_NAV_UL = ".site-nav ul {"


def check_mobile_css():
    with open(css_file) as f:
        css = f.read()
    # Check for mobile media query
    if MOBILE_MEDIA_QUERY not in css:
        print("FAIL: No mobile media query for nav")
        return False
    # Check for .site-nav and .site-nav ul inside mobile media query
    mobile_section = css.split(MOBILE_MEDIA_QUERY, 1)[-1]
    nav_ok = ".site-nav {" in mobile_section
    ul_ok = ".site-nav ul {" in mobile_section
    if not nav_ok:
        print("FAIL: No .site-nav { in mobile media query")
    if not ul_ok:
        print("FAIL: No .site-nav ul { in mobile media query")
    # Check that .site-nav ul is not display: none in mobile
    ul_block = "display: flex" in mobile_section or "display: block" in mobile_section
    if not ul_block:
        print("FAIL: .site-nav ul is not set to display:flex or block in mobile")
    return nav_ok and ul_ok and ul_block

def check_html_nav(file):
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
    # Check for at least 2 <li> in nav
    lis = ul.find_all("li")
    if len(lis) < 2:
        print(f"FAIL: Less than 2 <li> in nav in {file}")
        return False
    print(f"PASS: nav structure present in {file}")
    return True

def main():
    print("Checking mobile nav CSS...")
    css_ok = check_mobile_css()
    print("\nChecking nav HTML in outputs...")
    html_ok = all(check_html_nav(f) for f in files)
    if css_ok and html_ok:
        print("\nPASS: Mobile nav CSS and HTML structure detected.")
        sys.exit(0)
    else:
        print("\nFAIL: Mobile nav or CSS missing or broken.")
        sys.exit(1)

if __name__ == "__main__":
    main()
