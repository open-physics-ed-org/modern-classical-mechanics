#!/usr/bin/env python3
"""
fix_notebook_json_escapes.py

Auto-fix invalid JSON in Jupyter notebooks by escaping single backslashes in string values.
Usage: python3 fix_notebook_json_escapes.py <notebook.ipynb>
"""
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python3 fix_notebook_json_escapes.py <notebook.ipynb>")
    sys.exit(1)

infile = sys.argv[1]
with open(infile, 'r', encoding='utf-8') as f:
    raw = f.read()

# Escape single backslashes not already escaped (avoid \\)
# This is a simple heuristic and may not be perfect for all edge cases
fixed = re.sub(r'(?<!\\)\\(?![\\"/bfnrtu])', r'\\\\', raw)

with open(infile, 'w', encoding='utf-8') as f:
    f.write(fixed)

print(f"[FIXED] {infile}")
