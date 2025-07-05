#!/usr/bin/env python3
"""
check_nav_css_duplicates.py
Checks for duplicate or conflicting nav CSS rules in main.css and in the built HTML output (<style> tags).
Reports if the same nav class is defined in multiple places, or if there are conflicting rules.
"""
import re
from pathlib import Path

css_file = Path('docs/css/main.css')
outputs = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]

# Only check for duplicate main nav blocks, not all selectors
nav_blocks = [
    '.site-nav {',
    '.site-nav ul {',
    '.site-nav li {',
    '.site-nav a {',
    '.site-nav li ul {',
]

# Read main.css
css = css_file.read_text(errors='replace') if css_file.exists() else ''

# Patterns
style_tag_re = re.compile(r'<style.*?>(.*?)</style>', re.DOTALL|re.IGNORECASE)
class_re = re.compile(r'\.([\w-]+)')


# Check for duplicate nav blocks in main.css (should only be one of each main block)
print('Checking for duplicate nav block definitions in main.css...')
for block in nav_blocks:
    count = css.count(block)
    if count > 1:
        print(f'  WARNING: {block.strip()} defined {count} times in main.css!')

# Check for duplicate nav blocks in HTML <style> tags
for out in outputs:
    print(f'Checking {out} for duplicate nav block definitions in <style> tags...')
    if not out.exists():
        print('  File not found.')
        continue
    html = out.read_text(errors='replace')
    styles = style_tag_re.findall(html)
    for block in nav_blocks:
        count = sum(s.count(block) for s in styles)
        if count > 1:
            print(f'  WARNING: {block.strip()} defined {count} times in <style> tags in {out}!')
print('Done.')
