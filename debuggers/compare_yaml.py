#!/usr/bin/env python3
"""
Compare two YAML files for semantic (data) equality, ignoring formatting and key order.
Prints a summary and a diff if they differ.
"""
import sys
import yaml
import difflib
from pathlib import Path

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    if len(sys.argv) != 3:
        print("Usage: compare_yaml.py <file1.yaml> <file2.yaml>")
        sys.exit(1)
    file1, file2 = Path(sys.argv[1]), Path(sys.argv[2])
    if not file1.exists() or not file2.exists():
        print(f"[ERROR] One or both files do not exist: {file1}, {file2}")
        sys.exit(1)
    data1 = load_yaml(file1)
    data2 = load_yaml(file2)
    if data1 == data2:
        print(f"[OK] {file1.name} and {file2.name} are semantically identical.")
        sys.exit(0)
    else:
        print(f"[DIFF] {file1.name} and {file2.name} differ!")
        # Show a unified diff of the YAML text
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
        diff = difflib.unified_diff(lines1, lines2, fromfile=str(file1), tofile=str(file2))
        print(''.join(diff))
        sys.exit(2)

if __name__ == '__main__':
    main()
