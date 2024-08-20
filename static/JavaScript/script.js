document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        let menuIcons = document.querySelector('.menu-icons');
        let nav = document.querySelector('nav');

        if (menuIcons && nav) {
            menuIcons.addEventListener('click', () => {
                nav.classList.toggle('active');
            });
        } else {
            console.error('menuIcons or nav element not found');
        }
    }, 100); 
});