document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightboxImage');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const closeButton = document.querySelector('.lightbox .close');

    document.getElementById('galleryGrid').addEventListener('click', (e) => {
        if (e.target.tagName === 'IMG') {
            lightboxImage.src = e.target.src;
            lightboxCaption.textContent = e.target.alt;
            lightbox.style.display = 'block';
        }
    });

    closeButton.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });

    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
        }
    });
});