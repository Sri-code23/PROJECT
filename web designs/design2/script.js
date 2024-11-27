// JavaScript to control the navigation and page display

const navLinks = document.querySelectorAll('.navbar a'); // All the navbar links
const pages = document.querySelectorAll('.page'); // All the page sections

// Function to hide all pages and show the selected one
function showPage(pageId) {
    pages.forEach((page) => {
        page.classList.remove('active'); // Hide all pages
    });
    const activePage = document.getElementById(pageId);
    activePage.classList.add('active'); // Show the selected page
}

// Event listener for the navigation links
navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default link behavior
        const targetPage = link.getAttribute('href').substring(1); // Get the target section (remove the #)
        showPage(targetPage); // Call function to display the right page
    });
});

// Initial setup: Show the Home page and hide all other pages on load
window.addEventListener('load', () => {
    showPage('home'); // Show Home page by default
});
