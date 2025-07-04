# build_all.sh

This script runs all build steps for the Modern Classical Mechanics project in sequence, ensuring a fully reproducible workflow.

## What it does
- Fetches and relinks remote images for reproducibility
- Builds chapters (notebooks to Markdown, PDF, DOCX)
- Builds the full book (concatenated PDF/DOCX)
- Builds the static website (Jupyter Book)
- Ensures all images and figures are copied to the correct locations

## Usage
```bash
bash scripts/build_all.sh
```
