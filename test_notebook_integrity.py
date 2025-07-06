#!/usr/bin/env python3
"""
Test script: Ensure build-web.py does NOT modify any notebook files.
"""
import os
import hashlib
from pathlib import Path
import shutil
import subprocess

repo_root = Path(__file__).parent.resolve()
notebooks_dir = repo_root / 'notebooks'
backup_dir = repo_root / 'notebooks_backup_test'

# Step 1: Backup all notebooks
def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def backup_notebooks():
    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    backup_dir.mkdir()
    for nb in notebooks_dir.glob('*.ipynb'):
        shutil.copy2(nb, backup_dir / nb.name)

def compare_notebooks():
    for nb in notebooks_dir.glob('*.ipynb'):
        orig = backup_dir / nb.name
        if not orig.exists():
            print(f"[FAIL] Missing backup for {nb.name}")
            return False
        if hash_file(nb) != hash_file(orig):
            print(f"[FAIL] Notebook {nb.name} was modified!")
            return False
    print("[PASS] All notebooks unchanged after build-web.py run.")
    return True

if __name__ == '__main__':
    print("Backing up notebooks...")
    backup_notebooks()
    print("Running build-web.py...")
    subprocess.run(['python3', 'build-web.py'], check=True)
    print("Comparing notebooks...")
    ok = compare_notebooks()
    exit(0 if ok else 1)
