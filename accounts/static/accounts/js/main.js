
function togglePasswordVisibility(togglerId){
	const [, passwordElementName] = togglerId.split("-");
	const passwordElement = document.getElementById(`id_${passwordElementName}`);
	const toggleIcon = document.getElementById(`toggler-icon-${passwordElementName}`);
	
	if (passwordElement.type === 'password'){
		toggleIcon.className = 'far fa-eye';
		passwordElement.type = 'text';
	}else {
		toggleIcon.className = 'far fa-eye-slash';
		passwordElement.type = 'password';
	}
	console.log(toggleIcon);
}

const initialize = () => {
	const togglerElements = document.getElementsByClassName("password-toggler");

	for (let i=0; i < togglerElements.length; i++){
		togglerElements[i].addEventListener('click', function(){
			togglePasswordVisibility(this.id);
		}, false)
	}
}


window.addEventListener('load', initialize, false);