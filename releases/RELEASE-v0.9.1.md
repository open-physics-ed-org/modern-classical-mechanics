# RELEASE v0.9.1 "Persistent Poincaré" (July 2025)

**Mobile Menu, Docs, and Accessibility Improvements**

This release builds on v0.9 "Unified Unruh" with key usability, accessibility, and documentation improvements.

## 🚀 Highlights

- **Mobile Menu Accessibility:**
  - The navigation menu is now robustly scrollable and touch-friendly on all small/mobile screens. All menu items are accessible regardless of device size.
  - Improved z-index and overflow handling for mobile nav.
- **Documentation Streamlining:**
  - `README.md` and `build.md` have been further cleaned up, removing redundancy and clarifying theming, build, and usage instructions.
  - Theming and accessibility documentation is now concise and points to detailed guides.
- **Release Management:**
  - This release file follows the new pattern. The previous v0.9 release file is now only in the `releases/` folder.
- **Other Improvements:**
  - Minor accessibility and usability tweaks throughout the site and build system.
  - All changes are fully documented and committed.

## 🛠️ How to Upgrade

1. Pull the latest changes.
2. Review the updated `README.md`, `build.md`, and `content/announcement.md` for new features and instructions.
3. Use `python build.py --all` to build everything, or `python build.py --html` for just the web output.
4. All outputs are in `_build/` and `docs/`.

---

See the `releases/` folder for full historical release notes.
