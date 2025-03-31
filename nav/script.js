// JavaScript for the Navigation Indicator
const navLinks = document.querySelectorAll('.navigation ul li');
const indicator = document.querySelector('.indicator');

navLinks.forEach((link, index) => {
    link.addEventListener('click', () => {
        navLinks.forEach(item => item.classList.remove('active'));
        link.classList.add('active');
        indicator.style.transform = `translateX(${index * 70}px)`;
    });
});