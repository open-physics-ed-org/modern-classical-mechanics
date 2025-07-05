#!/usr/bin/env python3
"""
A minimal YAML-to-JSON converter for a very basic, well-formed YAML file.
This does NOT use any YAML library, just basic parsing for this specific menu structure.
Usage: ./basic_yaml2json.py _menu.yml > _menu.json
"""
import sys
import json

def parse_menu_yaml(filename):
    menu = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f if line.strip() and not line.strip().startswith('#')]
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('- title:'):
            title = line.split(':', 1)[1].strip()
            i += 1
            # Look ahead for path or children
            if i < len(lines) and 'path:' in lines[i]:
                path = lines[i].split(':', 1)[1].strip()
                menu.append({'title': title, 'path': path})
                i += 1
            elif i < len(lines) and 'children:' in lines[i]:
                i += 1
                children = []
                while i < len(lines) and lines[i].strip().startswith('- title:'):
                    child_title = lines[i].split(':', 1)[1].strip()
                    i += 1
                    if i < len(lines) and 'path:' in lines[i]:
                        child_path = lines[i].split(':', 1)[1].strip()
                        children.append({'title': child_title, 'path': child_path})
                        i += 1
                menu.append({'title': title, 'children': children})
            else:
                i += 1
        else:
            i += 1
    return {'menu': menu}

def main():
    if len(sys.argv) != 2:
        print("Usage: basic_yaml2json.py _menu.yml", file=sys.stderr)
        sys.exit(1)
    data = parse_menu_yaml(sys.argv[1])
    json.dump(data, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
