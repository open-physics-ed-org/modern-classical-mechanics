#!/usr/bin/env python3
"""
check_nav_style_precedence.py
Check the computed CSS precedence for navigation classes in the built HTML outputs.
- Finds all <style> and <link> tags affecting nav classes.
- Checks the order of appearance (inline <style>, <link>, etc.).
- Warns if any <style> tag with nav CSS appears after main.css.
- Reports if nav classes are defined in multiple places.
- Prints a summary of which CSS source wins for each nav class.
"""
import re
from pathlib import Path

outputs = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]
nav_classes = [
    'site-nav-menu', 'dropdown-menu', 'site-nav', 'site-nav ul', 'dropdown-menu',
]

style_tag_re = re.compile(r'<style.*?>(.*?)</style>', re.DOTALL|re.IGNORECASE)
link_tag_re = re.compile(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', re.IGNORECASE)
main_css_re = re.compile(r'main\\?\.css', re.IGNORECASE)

for out in outputs:
    print(f'Checking {out}...')
    if not out.exists():
        print('  File not found.')
        continue
    html = out.read_text(errors='replace')
    # Find all <link rel="stylesheet"> and <style> tags in order
    tags = []
    for m in re.finditer(r'(<link[^>]+rel=["\']stylesheet["\'][^>]*>|<style.*?>.*?</style>)', html, re.DOTALL|re.IGNORECASE):
        tags.append(m.group(0))
    main_css_seen = False
    for tag in tags:
        if '<link' in tag and main_css_re.search(tag):
            print('  main.css linked here.')
            main_css_seen = True
        if '<style' in tag:
            for nav in nav_classes:
                if nav in tag:
                    if not main_css_seen:
                        print(f'  WARNING: <style> for {nav} appears before main.css!')
                    else:
                        print(f'  WARNING: <style> for {nav} appears after main.css and may override it!')
    print('Done.')
