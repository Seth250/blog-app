
function toggleNavBar(){
    const navItems = document.querySelector('.nav-bar__items');
    navItems.classList.toggle('responsive-menu');
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