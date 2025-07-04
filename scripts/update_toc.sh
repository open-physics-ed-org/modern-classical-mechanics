#!/bin/bash
# update_toc.sh
# Generate _toc.yml for Jupyter Book from notebooks.yaml
# Usage: ./update_toc.sh

set -e

ROOT_DIR="$(dirname "$0")/.."
YAML_FILE="$ROOT_DIR/notebooks.yaml"
TOC_FILE="$ROOT_DIR/_toc.yml"

if [ ! -f "$YAML_FILE" ]; then
  echo "[ERROR] $YAML_FILE not found. Exiting."
  exit 1
fi

echo "# Auto-generated _toc.yml from notebooks.yaml" > "$TOC_FILE"
echo "format: jb-book" >> "$TOC_FILE"
echo "root: intro" >> "$TOC_FILE"
echo "chapters:" >> "$TOC_FILE"

# Extract notebook list and write to _toc.yml
awk '/^  - / { gsub(/.ipynb$/, "", $2); print "  - file: notebooks/" $2 }' "$YAML_FILE" >> "$TOC_FILE"

echo "[INFO] _toc.yml updated from notebooks.yaml."
