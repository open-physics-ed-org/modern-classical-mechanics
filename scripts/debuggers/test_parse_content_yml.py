#!/usr/bin/env python3
"""
Debugger script for parsing and inspecting _content.yml for build-web.manifest.py
- Prints all key sections and fields needed for the build system
- Logs output to debuggers/_content_parse_debug.log for review
- Add or modify print/log statements as needed for further debugging
"""
import yaml
from pathlib import Path
import sys
import datetime

LOG_PATH = Path(__file__).parent / '_content_parse_debug.log'

def log(msg):
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")
    print(msg)

def main():
    content_yml = Path(__file__).parent.parent / '_content.yml'
    if not content_yml.exists():
        log("ERROR: _content.yml not found!")
        sys.exit(1)

    log(f"Loading _content.yml from: {content_yml}")
    with open(content_yml, 'r') as f:
        try:
            data = yaml.safe_load(f)
            log("Successfully parsed _content.yml.")
        except Exception as e:
            log(f"YAML parse error: {e}")
            sys.exit(1)

    log("\n=== Site Metadata ===")
    for k, v in data.get('site', {}).items():
        log(f"{k}: {v}")

    log("\n=== Navigation ===")
    for item in data.get('navigation', []):
        log(f"- {item.get('title')} ({item.get('file', item.get('path', ''))})")

    log("\n=== Chapters ===")
    for chapter in data.get('chapters', []):
        log(f"Chapter {chapter.get('id', '?')}: {chapter.get('title', '')}")
        for fileinfo in chapter.get('files', []):
            log(f"  - {fileinfo.get('file')} (type: {fileinfo.get('type', '')}, title: {fileinfo.get('title', '')})")

    log("\n=== Homework ===")
    for hw in data.get('homework', []):
        log(f"- {hw.get('file')} (title: {hw.get('title', '')}, due: {hw.get('due', '')})")

    log("\n=== Output Formats and Directories ===")
    build = data.get('build', {})
    log(f"Outputs: {build.get('outputs', [])}")
    log(f"Output dir: {build.get('output_dir', '')}")
    log(f"Docs dir: {build.get('docs_dir', '')}")
    log(f"Sources dir: {build.get('sources_dir', '')}")
    log(f"Notebooks dir: {build.get('notebooks_dir', '')}")
    log(f"Static dir: {build.get('static_dir', '')}")
    log(f"Images dir: {build.get('images_dir', '')}")

    log("\n=== Static Resources ===")
    for k, v in data.get('static', {}).items():
        log(f"{k}:")
        for entry in v:
            if isinstance(entry, dict):
                log(f"  - {entry.get('path', entry)} ({entry.get('description', '')})")
            else:
                log(f"  - {entry}")

    log("\n=== Resources ===")
    for r in data.get('resources', []):
        log(f"- {r.get('file')} (title: {r.get('title', '')})")

    log("\n[DEBUG] _content.yml parsing complete. See this log for details.")

if __name__ == "__main__":
    main()
