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
    def parse_items(lines, start_idx, parent_indent):
        items = []
        idx = start_idx
        while idx < len(lines):
            line = lines[idx]
            if not line.strip():
                idx += 1
                continue
            indent = len(line) - len(line.lstrip(' '))
            stripped = line.strip()
            if indent <= parent_indent:
                break
            if stripped.startswith('- title:'):
                title = stripped.split(':', 1)[1].strip()
                item = {'title': title}
                idx += 1
                # Parse properties and children
                while idx < len(lines):
                    if idx >= len(lines):
                        break
                    prop_line = lines[idx]
                    prop_indent = len(prop_line) - len(prop_line.lstrip(' '))
                    prop_stripped = prop_line.strip()
                    if prop_indent <= indent:
                        break
                    if prop_stripped.startswith('path:'):
                        item['path'] = prop_stripped.split(':', 1)[1].strip()
                        idx += 1
                        continue
                    if prop_stripped.startswith('children:'):
                        # Recursively parse children
                        children = parse_items(lines, idx + 1, prop_indent)
                        item['children'] = children
                        # Move idx to after children
                        child_end = idx + 1
                        while child_end < len(lines):
                            child_line = lines[child_end]
                            child_indent = len(child_line) - len(child_line.lstrip(' '))
                            if child_indent <= prop_indent:
                                break
                            child_end += 1
                        idx = child_end
                        continue
                    idx += 1
                items.append(item)
            else:
                idx += 1
        return items

    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f if line.strip() and not line.strip().startswith('#')]
    # Find the root menu key and preserve hierarchy
    for idx, line in enumerate(lines):
        if line.strip().startswith('menu:'):
            # parse_items returns a list of top-level menu items
            menu = parse_items(lines, idx + 1, len(line) - len(line.lstrip(' ')))
            # If any item has 'children', keep as is; otherwise, just return as is
            return {'menu': menu}
    return {'menu': []}

def main():
    if len(sys.argv) != 2:
        print("Usage: basic_yaml2json.py _menu.yml", file=sys.stderr)
        sys.exit(1)
    data = parse_menu_yaml(sys.argv[1])
    json.dump(data, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
