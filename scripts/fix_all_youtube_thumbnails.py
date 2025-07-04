#!/usr/bin/env python3
"""
fix_all_youtube_thumbnails.py

Replace local YouTube thumbnail image links in all Jupyter notebooks with the correct remote thumbnail URL based on the video ID.
"""
import os
import json
import re

NOTEBOOK_DIR = "notebooks"

# Regex to match the local YouTube thumbnail markdown and extract the video ID from the link
YOUTUBE_IMG_PATTERN = re.compile(r'!\[.*?\]\(images/notes/week1//hqdefault.jpg\)\]\((https://(?:www\.)?youtube.com/watch\?v=([\w-]+))\)')
# Also match cases with only one closing parenthesis (for some markdown variants)
YOUTUBE_IMG_PATTERN_SIMPLE = re.compile(r'!\[.*?\]\(images/notes/week1//hqdefault.jpg\)')
YOUTUBE_LINK_PATTERN = re.compile(r'\[!\[YouTube thumbnail\]\(images/notes/week1//hqdefault.jpg\)\]\((https://(?:www\.)?youtube.com/watch\?v=([\w-]+))\)')

for root, _, files in os.walk(NOTEBOOK_DIR):
    for fname in files:
        if not fname.endswith('.ipynb'):
            continue
        path = os.path.join(root, fname)
        with open(path, 'r', encoding='utf-8') as f:
            try:
                nb = json.load(f)
            except Exception as e:
                print(f"[ERROR] Could not parse {path}: {e}")
                continue
        changed = False
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                new_source = []
                for line in cell.get('source', []):
                    # Replace the local thumbnail with the correct remote one if a YouTube link is present
                    m = re.search(r'\[!\[YouTube thumbnail\]\(images/notes/week1//hqdefault.jpg\)\]\((https://(?:www\.)?youtube.com/watch\?v=([\w-]+))\)', line)
                    if m:
                        video_id = m.group(2)
                        new_line = f"[![YouTube thumbnail](https://img.youtube.com/vi/{video_id}/hqdefault.jpg)]({m.group(1)})"
                        line = re.sub(r'\[!\[YouTube thumbnail\]\(images/notes/week1//hqdefault.jpg\)\]\(https://(?:www\.)?youtube.com/watch\?v=[\w-]+\)', new_line, line)
                        changed = True
                    # Also handle just the image (not a link)
                    elif re.search(YOUTUBE_IMG_PATTERN_SIMPLE, line):
                        # Try to find a YouTube link in the same cell
                        link_match = re.search(r'https://(?:www\.)?youtube.com/watch\?v=([\w-]+)', '\n'.join(cell.get('source', [])))
                        if link_match:
                            video_id = link_match.group(1)
                            new_line = f"![YouTube thumbnail](https://img.youtube.com/vi/{video_id}/hqdefault.jpg)"
                            line = re.sub(YOUTUBE_IMG_PATTERN_SIMPLE, new_line, line)
                            changed = True
                    new_source.append(line)
                cell['source'] = new_source
        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=4, ensure_ascii=False)
            print(f"[FIXED] {path}")
