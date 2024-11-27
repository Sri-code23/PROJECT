document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dragDropZone');
    const fileInput = document.getElementById('fileInput');
    const imagePreview = document.getElementById('imagePreview');
    const uploadButton = document.getElementById('uploadButton');
    const uploadForm = document.getElementById('imageUploadForm');

    // Drag and drop functionality
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('drag-over');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over');
        handleFiles(e.dataTransfer.files);
    });

    fileInput.addEventListener('change', () => {
        handleFiles(fileInput.files);
    });

    function handleFiles(files) {
        if (files.length > 0) {
            const file = files[0];
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    imagePreview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
                    uploadButton.disabled = false;
                };
                reader.readAsDataURL(file);
            } else {
                alert('Please select an image file.');
            }
        }
    }

    uploadForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Add your upload logic here
        console.log('Image uploaded');
        // Reset form after upload
        uploadForm.reset();
        imagePreview.innerHTML = '';
        uploadButton.disabled = true;
    });
});