# Script: fetch_remote_images.sh

## Purpose

Automates the process of downloading all remote images referenced in Jupyter notebooks and updates the notebook/chapter links to use local copies. This ensures all assets are available for offline builds and publication.

## How It Works
- Scans all notebooks in the `notebooks/` directory for image links pointing to remote URLs.
- Downloads each remote image to the appropriate local images directory (e.g., `notebooks/images/notes/week1/`).
- Updates the notebook files to reference the downloaded local images instead of the remote URLs.
- Can be run independently or as part of the build scripts.

## Usage

```bash
./scripts/fetch_remote_images.sh
```

This script is automatically called by all main build scripts (`build_chapters.sh`, `build_book.sh`, `build_website.sh`, `build_all.sh`).

## Implementation Notes
- Compatible with macOS and Linux (uses `sed` and `wget`/`curl`).
- Ensures idempotency: running multiple times does not duplicate downloads or relinking.
- Handles errors gracefully and logs missing or failed downloads.

## See Also
- [build_chapters.sh](scripts_build_chapters.md)
- [build_website.sh](scripts_build_website.md)
- [build_all.sh](scripts_build_all.md)
