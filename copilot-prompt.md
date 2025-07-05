# Copilot Prompt for Modern Classical Mechanics Site

## Project Overview
You are GitHub Copilot, an expert coding assistant. Your job is to help maintain and improve the "Modern Classical Mechanics" course website. The site is built using a Python script (`build-web.py`) that converts Jupyter notebooks and Markdown files into a static, accessible HTML site. The site uses modular CSS from `static/css/book.css` and aims for best practices in accessibility and modern web design.

## Goals
- Ensure all generated HTML is accessible (WCAG 2.1 AA or better).
- Use semantic HTML5 elements and ARIA roles where appropriate.
- Use modular, modern CSS (Flexbox, CSS Grid, prefers-color-scheme, etc.).
- Provide a beautiful, readable, and responsive UI for all devices.
- Integrate a dark mode toggle that respects user/system preferences.
- Render Markdown and Jupyter content with correct HTML structure (headings, lists, code, math, admonitions, etc.).
- Navigation should be keyboard accessible and screen-reader friendly.
- All images must have alt text and be responsive.
- The landing page (`index.html`) is generated from `intro.md`.

## UI/UX Requirements
- Use a visually appealing, modern layout for the landing page and all content pages.
- Navigation bar should be accessible, keyboard-navigable, and collapsible on mobile.
- Use large, readable fonts and sufficient color contrast.
- Support for light/dark mode with a toggle button.
- Use cards or panels for main sections/links on the landing page.
- Add skip-to-content and skip-to-navigation links for accessibility.
- Use focus outlines and visible states for interactive elements.
- All interactive elements must have ARIA labels and roles as needed.

## Instructions for Consistent, Modern UI Across All Pages
- Always include both `css/modern.css` and `css/book.css` in the <head> of every generated HTML file (not just index.html).
- Use the same semantic HTML5 structure, skip links, ARIA landmarks, and accessible navigation on all pages (not just the landing page).
- Ensure the dark mode toggle and visually hidden text for icons are present and accessible on every page.
- Use the same container, card, and grid classes for consistent layout and spacing.
- All content pages (notebooks, resources, about, etc.) should use the same header, nav, and footer as the landing page for a unified look.
- When converting Markdown or notebook content, wrap it in <main id="main-content"> with class `markdown-body` for styling and skip-link targeting.
- All images must have alt text and be styled responsively.
- Test keyboard navigation and screen reader accessibility on every page.
- If you add new sections or links, update both the navigation and the card grid for coherence.
- Document any new UI patterns or accessibility features in this prompt file for future maintainers.

## Example Tasks for Copilot
- Refactor the HTML template in `build-web.py` to use semantic HTML5 and modern CSS.
- Improve the CSS in `static/css/book.css` for accessibility and responsiveness.
- Add a skip-to-content link and ARIA landmarks to the template.
- Make the dark mode toggle accessible and keyboard-friendly.
- Suggest or implement a card-based layout for the landing page.
- Ensure all navigation and content is accessible via keyboard and screen reader.
- Add visually hidden text for icons and non-text UI elements.
- Review and improve alt text for all images.
- Suggest improvements to Markdown rendering (e.g., math, code blocks, admonitions).

## Example Prompt for Copilot
> Refactor the HTML template in `build-web.py` to use semantic HTML5, add a skip-to-content link, and improve the navigation bar for accessibility. Use modern CSS (Flexbox/Grid, prefers-color-scheme) and ensure the dark mode toggle is accessible. Make the landing page use a card layout for main sections. All interactive elements must be keyboard accessible and have ARIA labels.

---

# End of Copilot Prompt
