document.addEventListener('DOMContentLoaded', () => {
    const galleryGrid = document.getElementById('galleryGrid');
    const searchInput = document.getElementById('searchInput');
    const filterSelect = document.getElementById('filterSelect');

    // Dummy data for demonstration
    const images = [
        { id: 1, src: 'path/to/image1.jpg', caption: 'Image 1', tags: ['nature', 'landscape'] },
        { id: 2, src: 'path/to/image2.jpg', caption: 'Image 2', tags: ['urban', 'city'] },
        // Add more image objects as needed
    ];

    function renderGallery(images) {
        galleryGrid.innerHTML = '';
        images.forEach(image => {
            const imageElement = document.createElement('div');
            imageElement.classList.add('gallery-item');
            imageElement.innerHTML = `
                <img src="${image.src}" alt="${image.caption}" data-id="${image.id}">
                <p>${image.caption}</p>
            `;
            galleryGrid.appendChild(imageElement);
        });
    }

    function filterImages() {
        const searchTerm = searchInput.value.toLowerCase();
        const filterTag = filterSelect.value;
        
        const filteredImages = images.filter(image => {
            const matchesSearch = image.caption.toLowerCase().includes(searchTerm);
            const matchesTag = filterTag === '' || image.tags.includes(filterTag);
            return matchesSearch && matchesTag;
        });

        renderGallery(filteredImages);
    }

    searchInput.addEventListener('input', filterImages);
    filterSelect.addEventListener('change', filterImages);

    // Initial render
    renderGallery(images);
});