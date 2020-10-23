
function toggleNavBar(){
    if (window.matchMedia("(max-width: 600px)").matches) {
        const navItems = document.querySelector('.nav-bar__items');
        navItems.classList.toggle('responsive-menu');
        document.querySelector('.page-wrapper').classList.toggle('scroll-lock');
    }
}

function initialize(){
    const messageBox = document.querySelector('.message-container');
    if (messageBox){
        const close = document.querySelector('.close');
        close.addEventListener('click', () => messageBox.classList.add('hide'), false);
    }

    const hamburgerMenu = document.querySelector('.nav-bar__hamburger');
    hamburgerMenu.addEventListener('click', toggleNavBar, false);
}

window.addEventListener('load', initialize, false);