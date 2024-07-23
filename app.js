// Selectors
const hamburger = document.querySelector('.hamburger');
const themeToggleBtn = document.querySelector('.theme-toggle');
const navList = document.querySelector('.nav__list');
const navItems = document.querySelectorAll('.nav__item');

// States
const theme = localStorage.getItem('theme');

// On mount
theme && document.body.classList.add(theme);

// Functions
const handleThemeToggle = () => {
    document.body.classList.toggle('darkmode');
    if (document.body.classList.contains('darkmode')) {
        localStorage.setItem('theme', 'darkmode');
    } else {
        localStorage.removeItem('theme');
    }
};

// Events
hamburger.onclick = () => navList.classList.toggle('active');
themeToggleBtn.addEventListener('click', handleThemeToggle);

navItems.forEach(element => element.onclick = () => {
    navList.classList.remove('active');
});