#!/usr/bin/env python3
"""
A standalone script to convert a YAML file to JSON using ruamel.yaml (not PyYAML).
Usage: ./yaml2json.py input.yml > output.json
"""
import sys
import json
from ruamel.yaml import YAML

def main():
    if len(sys.argv) != 2:
        print("Usage: yaml2json.py input.yml", file=sys.stderr)
        sys.exit(1)
    infile = sys.argv[1]
    with open(infile, 'r', encoding='utf-8') as f:
        yaml = YAML(typ='safe')
        data = yaml.load(f)
    json.dump(data, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
