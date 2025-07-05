#!/usr/bin/env python3
"""
auto_clean_nav_css.py
Removes all legacy/mobile nav CSS blocks (side-nav, side-menu, menu-toggle) from a CSS file.
Backs up the original file as <file>.bak.
"""
import re
from pathlib import Path

CSS_PATH = Path('static/css/main.css')
BACKUP_PATH = CSS_PATH.with_suffix('.css.bak')

# Patterns to remove: selectors and blocks for .side-nav, .side-menu, .menu-toggle (standalone and nested)
REMOVE_PATTERNS = [
    r'(?s)\/\*.*?\*\/\s*',  # Remove comments (optional, for clarity)
    r'\.(side-nav|side-menu|menu-toggle)[^,{]*\{[^}]*\}',  # Standalone blocks
    r'\.(side-nav|side-menu|menu-toggle)[^,{]*,[^\{]*\{[^}]*\}',  # Multi-selector blocks
    r'@media[^{]+\{[^}]*\.(side-nav|side-menu|menu-toggle)[^,{]*\{[^}]*\}[^}]*\}',  # Media queries with these selectors
    r'\.(side-nav|side-menu|menu-toggle)[^,]*,',  # Remove from selector lists
    r',\s*\.(side-nav|side-menu|menu-toggle)[^,{]*',  # Remove from selector lists (trailing)
]

css = CSS_PATH.read_text(errors='replace')
BACKUP_PATH.write_text(css)

for pat in REMOVE_PATTERNS:
    css = re.sub(pat, '', css)

# Remove empty lines and excessive whitespace
css = re.sub(r'\n\s*\n', '\n', css)
css = re.sub(r'\n{3,}', '\n\n', css)

CSS_PATH.write_text(css)
print(f"Cleaned {CSS_PATH}, backup at {BACKUP_PATH}")
