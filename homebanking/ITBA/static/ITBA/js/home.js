//Prueba de Login
function recogeDatos(e) {
  e.preventDefault();

  let usernameLogin = document.querySelector("#usernameLogin").value;
  console.log(username + " ah iniciado sesión");
  let usernameLogged = document.querySelector("#usernameLogged");
  usernameLogged.textContent = usernameLogin;
}

let miForm = document.querySelector("#inicio-sesion");

// miForm.addEventListener("submit", recogeDatos);

//Perfil
function menuToggle() {
  const toggleMenu = document.querySelector(".menu-p");
  toggleMenu.classList.toggle("active-p");
}
