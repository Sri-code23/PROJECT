const menuIcon = document.getElementById('menuIcon');
const popupMenu = document.getElementById('popupMenu');

menuIcon.addEventListener('click', () => {
    if (popupMenu.style.left === '-100%') {
        popupMenu.style.left = '0';
    } else {
        popupMenu.style.left = '-100%';
    }
});
