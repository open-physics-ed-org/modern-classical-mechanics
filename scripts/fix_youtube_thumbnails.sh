#!/bin/bash
# fix_youtube_thumbnails.sh
# Replace local hqdefault.jpg YouTube thumbnails with remote images using the video ID

set -e

NOTEBOOK_DIR="notebooks"

find "$NOTEBOOK_DIR" -name '*.ipynb' | while read -r nb; do
    echo "Processing $nb ..."
    # Use Python to do the replacement robustly
    python3 - <<ENDPYTHON "$nb"
import sys
import json
import re

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

changed = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'markdown':
        new_source = []
        for line in cell.get('source', []):
            # Find YouTube links
            yt_match = re.search(r'https://(?:www\.)?youtube\.com/watch\?v=([\w-]+)', line)
            if yt_match:
                video_id = yt_match.group(1)
                # Replace local image with remote thumbnail
                line = re.sub(r'\!\[.*?\]\(images/notes/week1//hqdefault.jpg\)',
                              f'![YouTube thumbnail](https://img.youtube.com/vi/{video_id}/hqdefault.jpg)',
                              line)
                changed = True
            new_source.append(line)
        cell['source'] = new_source

if changed:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=4, ensure_ascii=False)
    print(f"Updated: {path}")
ENDPYTHON
done

echo "All YouTube thumbnails updated to use remote images."
