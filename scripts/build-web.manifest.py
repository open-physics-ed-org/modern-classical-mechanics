#!/usr/bin/env python3
# build-web.manifest.py (copied to scripts/ for robust editing and testing)
# See original in project root for full context and history.

# --- Build resources.html from resources.md and about.html from about.md ---
    # (Code moved inside main() after all variables are defined)
from pathlib import Path
# --- Global paths (needed by all functions) ---
repo_root = Path(__file__).parent.parent.resolve()
autogen_dir = repo_root / '.autogen'
docs_dir = repo_root / 'docs'
build_dir = repo_root / '_build' / 'wcag-html'
notebooks_dir = repo_root / 'content' / 'notebooks'
build_dir.mkdir(parents=True, exist_ok=True)
docs_dir.mkdir(parents=True, exist_ok=True)
nojekyll = docs_dir / '.nojekyll'
if not nojekyll.exists():
    nojekyll.touch()

import os
import shutil
import hashlib
import requests
import nbformat
from pathlib import Path
from nbconvert import HTMLExporter
import bs4
import subprocess
import json
import yaml

# --- Use robust basic_yaml2json.py from scripts/ ---
def menu_json_from_yaml(menu_yml_path):
    """Convert YAML menu to JSON using robust scripts/basic_yaml2json.py."""
    script_path = repo_root / 'scripts' / 'basic_yaml2json.py'
    try:
        result = subprocess.run([
            'python3', str(script_path), str(menu_yml_path)
        ], capture_output=True, check=True)
        menu_json = result.stdout.decode('utf-8')
        return json.loads(menu_json)
    except Exception as e:
        print(f'[ERROR] Could not convert _menu.yml to JSON using scripts/basic_yaml2json.py: {e}')
        return None

# ...rest of the code is identical to the original build-web.manifest.py...
# (You can now safely edit and test this version in scripts/)
