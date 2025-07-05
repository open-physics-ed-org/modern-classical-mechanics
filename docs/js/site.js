// Modern Classical Mechanics site-wide JS
// Accessibility and UI helpers

// Dark mode toggle
function toggleDark() {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
}
if (localStorage.getItem('theme') === 'dark') {
  document.documentElement.classList.add('dark');
}

// Keyboard accessibility for dark mode toggle
const darkToggle = document.querySelector('.toggle-dark');
if (darkToggle) {
  darkToggle.addEventListener('keyup', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleDark();
    }
  });
}

// Focus style for skip links
const skipLinks = document.querySelectorAll('.skip-link');
skipLinks.forEach(link => {
  link.addEventListener('focus', function() {
    this.classList.add('skip-link-focus');
  });
  link.addEventListener('blur', function() {
    this.classList.remove('skip-link-focus');
  });
});

// Optional: Collapse/expand nav for mobile (if you add a hamburger menu)
// ...
