const navLinks = document.querySelectorAll('.navbar a'); // All the navbar links
const pages = document.querySelectorAll('.page'); // All the page sections

navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent the default link behavior
        
        const targetPage = link.getAttribute('href').substring(1); // Get the target section (remove the #)

        // Hide all pages
        pages.forEach((page) => {
            page.style.display = 'none'; // Hide each page
        });

        // Show the target page
        const activePage = document.getElementById(targetPage);
        activePage.style.display = 'block'; // Show the selected page
    });
});

// Initial setup: Show the Home page and hide all other pages on load
window.addEventListener('load', () => {
    pages.forEach((page, index) => {
        if (index === 0) {
            page.style.display = 'block'; // Show Home page by default
        } else {
            page.style.display = 'none'; // Hide all other pages
        }
    });
});
