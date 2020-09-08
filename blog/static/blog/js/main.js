function delegateClickEvent(event){
    if (event.target.matches('.like-toggler')){
        event.preventDefault();
        oppElem = event.target.nextElementSibling;
        objectActionToggle(event.target, oppElem);
    } else if (event.target.matches('.dislike-toggler')){
        event.preventDefault();
        oppElem = event.target.previousElementSibling;
        objectActionToggle(event.target, oppElem);
    }
}

function objectActionToggle(eventTarget, oppElem){
    if (oppElem.classList.contains('selected')) {
        oppElem.classList.remove('selected');
        --oppElem.querySelector('span').textContent;
        eventTarget.classList.add('selected');
        ++eventTarget.querySelector('span').textContent;
    } else if (eventTarget.classList.contains('selected')){
        eventTarget.classList.remove('selected');
        --eventTarget.querySelector('span').textContent;
    } else {
        eventTarget.classList.add('selected');
        ++eventTarget.querySelector('span').textContent;
    }

    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch(eventTarget.href, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken
        }
    // }).then((response) => response.ok ? response.json() : Promise.reject(response))
    //   .then((data) => console.log(data))
      }).catch((err) => console.log(err));
}

const initialize = () => {
    const postDetail = document.querySelector('.post-detail');
    postDetail.addEventListener('click', delegateClickEvent, false);
}

window.addEventListener('load', initialize, false);