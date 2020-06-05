
function togglePasswordVisibility(elementId){
	const elementName = JSON.stringify(elementId.split("-").slice(-1))
	console.log(elementName)
	// let passwordElement = document.getElementById(`id_${}`);
	// let toggleIcon = document.getElementById(`toggler-icon-{id}`);
	// // console.log(passwordElement, toggleIcon);
	// if (passwordElement.type === 'password'){
	// 	toggleIcon.className = 'far fa-eye';
	// 	passwordElement.type = 'text';
	// }else {
	// 	toggleIcon.className = 'far fa-eye-slash';
	// 	passwordElement.type = 'password';
	// }
}

function initialize(){
	let togglerElements = document.getElementsByClassName("password-toggler");
	// console.log(togglerElements);

	for (let i=0; i < togglerElements.length; i++){
		togglerElements[i].addEventListener('click', () => {
			togglePasswordVisibility(togglerElements[i].id)
		}, false)
	}
	// togglerElements.forEach((element) => {
	// 	element.addEventListener('click', function(){
	// 		togglePasswordVisibility(element.id)
	// 	}, false)
	// })
}

window.addEventListener('load', initialize, false);