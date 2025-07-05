#!/usr/bin/env python3
"""
check_nav_css_overrides.py
Check if navigation-related CSS classes (.site-nav-menu, .dropdown-menu, .site-nav, .site-nav ul, etc.) are being overridden or injected by build-web.py or in the built HTML output.

Checks:
- Look for <style> tags or inline <style> in docs/index.html and _build/html/index.html that override nav CSS.
- Look for <style> or <link> tags injected by build-web.py that might override main.css nav rules.
- Look for nav-related classes in <style> tags in the HTML output.
- Print any suspicious overrides or duplications.
"""
import re
from pathlib import Path

# Files to check
outputs = [
    Path('docs/index.html'),
    Path('_build/html/index.html'),
]

# Nav classes to check
nav_classes = [
    'site-nav-menu', 'dropdown-menu', 'site-nav', 'site-nav-menu', 'site-nav ul', 'dropdown-menu',
]

# Patterns
style_tag_re = re.compile(r'<style.*?>(.*?)</style>', re.DOTALL|re.IGNORECASE)
link_tag_re = re.compile(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', re.IGNORECASE)
class_re = re.compile(r'\.([\w-]+)')

for out in outputs:
    print(f'Checking {out}...')
    if not out.exists():
        print('  File not found.')
        continue
    html = out.read_text(errors='replace')
    # Find all <style> tags
    styles = style_tag_re.findall(html)
    if styles:
        for s in styles:
            for nav in nav_classes:
                if nav in s:
                    print(f'  POSSIBLE OVERRIDE: <style> tag contains {nav} in {out}')
    # Find all <link rel="stylesheet"> tags
    links = link_tag_re.findall(html)
    for link in links:
        if 'main.css' not in link:
            print(f'  WARNING: Non-main.css stylesheet linked: {link}')
    # Look for nav classes in inline style attributes
    if 'style=' in html:
        for nav in nav_classes:
            if nav in html:
                print(f'  POSSIBLE INLINE STYLE OVERRIDE: {nav} found in style attribute in {out}')
    # Look for nav classes in <style> tags
    for s in styles:
        for nav in nav_classes:
            if nav in s:
                print(f'  <style> tag in {out} contains {nav}')
    print('Done.')
