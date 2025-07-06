#!/usr/bin/env python3
"""
Test script: Ensure all HTML image references in docs/ are valid and images are referenced simply and correctly.
"""
import re
from pathlib import Path
import sys

repo_root = Path(__file__).parent.resolve()
docs_dir = repo_root / 'docs'
images_dir = docs_dir / 'images'

# Helper: check for simple filenames (no spaces, all lowercase, no special chars except -_.)
def is_simple_name(name):
    return re.match(r'^[a-z0-9_.-]+$', name) is not None

def get_html_image_refs():
    refs = []
    for html_file in docs_dir.glob('*.html'):
        with open(html_file, encoding='utf-8') as f:
            content = f.read()
        # Find all src="..." and src='...'
        for m in re.findall(r'src=["\']([^"\']+)["\']', content):
            if m.startswith('http') or m.startswith('data:'):
                continue
            refs.append((html_file.name, m))
    return refs

def main():
    refs = get_html_image_refs()
    missing = []
    not_simple = []
    for html, ref in refs:
        # Only check images in images_dir
        if not ref.startswith('images/'):
            print(f"[WARN] {html} references non-images/ resource: {ref}")
            continue
        img_name = Path(ref).name
        img_path = images_dir / img_name
        if not img_path.exists():
            missing.append((html, ref))
        if not is_simple_name(img_name):
            not_simple.append((html, ref))
    if missing:
        print("[FAIL] Missing images:")
        for html, ref in missing:
            print(f"  {html}: {ref}")
    else:
        print("[PASS] All referenced images exist.")
    if not_simple:
        print("[WARN] Non-simple image names:")
        for html, ref in not_simple:
            print(f"  {html}: {ref}")
    else:
        print("[PASS] All image names are simple.")
    # Optionally: check for unused images
    referenced = set(Path(ref).name for _, ref in refs if ref.startswith('images/'))
    unused = [img.name for img in images_dir.glob('*') if img.name not in referenced]
    if unused:
        print("[INFO] Unused images in images/: ")
        for name in unused:
            print(f"  {name}")
    else:
        print("[PASS] All images in images/ are referenced.")
    # Exit code: fail if missing images
    sys.exit(1 if missing else 0)

if __name__ == '__main__':
    main()
