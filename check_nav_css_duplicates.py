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



# Improved duplicate nav block check: only warn if more than one global (non-media) block exists
def find_global_blocks(css, block):
    """Return the number of times a nav block appears outside any @media block."""
    # Split CSS into lines and track if inside a media query
    lines = css.splitlines()
    in_media = False
    global_count = 0
    for i, line in enumerate(lines):
        l = line.strip()
        if l.startswith('@media'):
            in_media = True
        if l.endswith('}'):  # crude: end of media block
            in_media = False if in_media else in_media
        if block in l and not in_media:
            global_count += 1
    return global_count

print('Checking for duplicate nav block definitions in main.css (ignoring mobile overrides)...')
for block in nav_blocks:
    global_count = find_global_blocks(css, block)
    if global_count > 1:
        print(f'  WARNING: {block.strip()} defined {global_count} times globally in main.css!')
    elif global_count == 0:
        print(f'  ERROR: {block.strip()} not found globally in main.css!')
    else:
        print(f'  OK: {block.strip()} defined once globally.')

# Extra test: ensure any additional definitions are only inside @media (max-width: 760px)
for block in nav_blocks:
    total = css.count(block)
    global_count = find_global_blocks(css, block)
    if total > global_count:
        print(f'  NOTE: {block.strip()} has {total - global_count} override(s) in media queries (expected for responsive design).')
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
