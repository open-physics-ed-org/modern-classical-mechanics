# fetch_remote_images.sh

Automates the process of downloading all remote images referenced in Jupyter notebooks and updates the notebook/chapter links to use local copies. This ensures all assets are available for offline builds and publication.

## What it does
- Scans all notebooks in the `notebooks/` and `chapters/` directories for image links pointing to remote URLs.
- Downloads each remote image to the appropriate local images directory (e.g., `notebooks/images/notes/week1/`).
- Updates the notebook files to reference the downloaded local images instead of the remote URLs.
- Can be run independently or as part of the build scripts.

## Usage
```bash
bash scripts/fetch_remote_images.sh
```
