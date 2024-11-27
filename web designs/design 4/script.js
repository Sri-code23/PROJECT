// Script to handle page navigation between sections
document.addEventListener("DOMContentLoaded", function() {
    const pages = document.querySelectorAll(".page");
    const links = document.querySelectorAll(".navbar a");

    // Function to hide all pages and display the active one
    function showPage(targetId) {
        pages.forEach(page => {
            if (page.id === targetId) {
                page.classList.add("active"); // Display the active page
            } else {
                page.classList.remove("active"); // Hide the other pages
            }
        });
    }

    // Set default active page (home)
    showPage("home");

    // Event listener for navbar clicks
    links.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault(); // Prevent default anchor behavior
            const targetId = this.getAttribute("href").substring(1); // Get the section ID from href
            showPage(targetId); // Show the corresponding page
        });
    });
});

// Smooth hover animation for the project boxes
const projectBoxes = document.querySelectorAll(".project-box");
projectBoxes.forEach(box => {
    box.addEventListener("mouseenter", function() {
        this.style.transform = "scale(1.05)";
        this.style.boxShadow = "0px 6px 15px rgba(0, 0, 0, 0.3)";
    });
    box.addEventListener("mouseleave", function() {
        this.style.transform = "scale(1)";
        this.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.2)";
    });
});
