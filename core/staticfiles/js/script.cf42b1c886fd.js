let navbar = document.querySelector('.header .navbar');
let searchForm = document.querySelector('.header .search-form');
let contactInfo = document.querySelector('.contact-info');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
};

window.onscroll = () => {
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
    contactInfo.classList.remove('active');
};

var swiper = new Swiper('.blog-slider', {
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
});