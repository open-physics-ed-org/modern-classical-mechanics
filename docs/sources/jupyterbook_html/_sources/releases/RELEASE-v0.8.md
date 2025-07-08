# Release v0.8 "Noble Noether" (July 2025)

## 🚀 Major Improvements

- **Navigation and accessibility overhaul:**
  - Main navigation menu is now fully accessible, visually consistent, and all top-level items are links.
  - Desktop: larger nav text, even spacing, improved dark mode, and no hamburger menu.
  - Mobile: navigation is a fixed bottom bar with a modern, accessible submenu popup.
- **Download buttons:**
  - Download links for chapter sources are now visually distinct, accessible buttons with clear icons and WCAG-compliant styles.
- **Release notes organization:**
  - All historical release notes are now available as markdown files in the `releases/` folder, generated directly from GitHub releases.
- **Build and menu improvements:**
  - `build-web.py` updated to generate correct menu HTML and download buttons, using representative emojis for each file type.
  - `_menu.yml` ensures all top-level nav items are links and styled consistently.

## 🐛 Bug Fixes & Accessibility

- **Mobile menu and submenu usability:**
  - Submenus now appear as a full-width popup above the bottom nav, with touch-friendly spacing and no overlap.
  - Improved color contrast and focus states for all nav and download buttons in both light and dark mode.
- **General accessibility:**
  - All interactive elements are keyboard accessible and have visible focus styles.

## 📝 How to use

- Run the build as usual:
  ```sh
  python build-web.py
  ```
- All navigation and download features will be present in the generated site.
- See the [README.md](../README.md) for full project details and build instructions.

---

**Release date:** July 2025

---

## Highlights

- **Navigation:**
  - Desktop: accessible, large, evenly spaced nav links; no hamburger menu.
  - Mobile: fixed bottom bar, accessible submenu popup.
- **Download buttons:**
  - Accessible, visually distinct, and consistent across all chapters.
- **Release notes:**
  - All releases from v0.1 to v0.8 are now available as markdown files in `releases/`.

---

See the [README.md](../README.md) for full project details and build instructions.
