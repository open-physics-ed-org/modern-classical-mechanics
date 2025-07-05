#!/usr/bin/env python3
"""
check_nav_html_css_match.py
Checks that every nav class in the HTML output is defined in main.css, and that no nav class is defined only in <style> tags in the HTML output.
Warns if any nav class is present in HTML but not in main.css, or if any nav class is defined in a <style> tag but not in main.css.
"""
import re
from pathlib import Path

# Files
outputs = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]
css_file = Path('docs/css/main.css')

# Nav classes to check
nav_classes = [
    'site-nav-menu', 'dropdown-menu', 'site-nav', 'site-nav ul', 'dropdown-menu',
]

# Read main.css
css = css_file.read_text(errors='replace') if css_file.exists() else ''

# Patterns
style_tag_re = re.compile(r'<style.*?>(.*?)</style>', re.DOTALL|re.IGNORECASE)
class_re = re.compile(r'\.([\w-]+)')

for out in outputs:
    print(f'Checking {out}...')
    if not out.exists():
        print('  File not found.')
        continue
    html = out.read_text(errors='replace')
    # Find all nav classes in HTML
    found = set()
    for nav in nav_classes:
        if nav in html:
            found.add(nav)
    # Check if each found class is in main.css
    for nav in found:
        if nav not in css:
            print(f'  WARNING: {nav} present in HTML but not in main.css!')
    # Check for nav classes in <style> tags
    styles = style_tag_re.findall(html)
    for s in styles:
        for nav in nav_classes:
            if nav in s and nav not in css:
                print(f'  WARNING: {nav} defined in <style> tag but not in main.css!')
    print('Done.')
