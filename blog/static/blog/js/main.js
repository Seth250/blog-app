
function delegateClickEvent(event){
    if (event.target.matches('.like-toggler')){
        event.preventDefault();
        const oppElem = event.target.nextElementSibling;
        objectActionToggle(event.target, oppElem);
    } else if (event.target.matches('.dislike-toggler')){
        event.preventDefault();
        const oppElem = event.target.previousElementSibling;
        objectActionToggle(event.target, oppElem);
    }
}

function objectActionToggle(eventTarget, oppElem){
    if (oppElem.classList.contains('selected')) {
        oppElem.classList.remove('selected');
        eventTarget.classList.add('selected');
    } else {
        eventTarget.classList.toggle('selected');
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
    }).then((response) => response.ok ? response.json() : Promise.reject(response))
      .then(({ main_elem_count, opp_elem_count}) => {
        eventTarget.querySelector('span').textContent = main_elem_count;
        oppElem.querySelector('span').textContent = opp_elem_count;
      })
      .catch((err) => errorHandler(err));
}

async function errorHandler(error){
    if (error.status){
        const { redirect_url } = await error.json();
        window.location.href = redirect_url
    } else {
        console.error(error);
    }
}

const main = () => {
    const postDetail = document.querySelector('.post-detail');
    postDetail.addEventListener('click', delegateClickEvent, false);
}

window.addEventListener('load', main, false);