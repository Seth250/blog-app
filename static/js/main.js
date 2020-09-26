
function initialize(){
    const messageBox = document.querySelector('.message-container');
    if (messageBox){
        const close = document.querySelector('.close');
        close.addEventListener('click', () => messageBox.classList.add('hide'), false);
    }
}

window.addEventListener('load', initialize, false);