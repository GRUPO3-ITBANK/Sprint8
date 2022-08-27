let submenu1 = document.getElementById("submenu1");
let submenu2 = document.getElementById("submenu2");
let submenu3 = document.getElementById("submenu3");

function desplegarHamburguesa() {
  let desplegable = document.getElementById("menu");

  if (desplegable.classList.contains("menu-active")) {
    desplegable.classList.remove("menu-active");
    desplegable.classList.add("menu-inactive");
  } else if (desplegable.classList.contains("menu-inactive")) {
    desplegable.classList.add("menu-active");
    desplegable.classList.remove("menu-inactive");
  }
}

document.addEventListener("click", () => {
  submenu1.classList.remove();
});

function desplegarSubmenu(desplegable) {
  function toggle(desplegable) {
    if (desplegable.classList.contains("submenu-active")) {
      desplegable.classList.remove("submenu-active");
      desplegable.classList.add("submenu-inactive");
    } else if (desplegable.classList.contains("submenu-inactive")) {
      desplegable.classList.add("submenu-active");
      desplegable.classList.remove("submenu-inactive");
      desplegable.classList.add("slide-in-top");
    }
  }
  function cierreDemasDesplegables(d1, d2) {
    d1.classList.remove("submenu-active");
    d1.classList.add("submenu-inactive");
    d2.classList.remove("submenu-active");
    d2.classList.add("submenu-inactive");
  }

  if (desplegable == "submenu1") {
    let desplegable = submenu1;
    toggle(desplegable);
    cierreDemasDesplegables(submenu2, submenu3);
  } else if (desplegable == "submenu2") {
    let desplegable = document.getElementById("submenu2");
    toggle(desplegable);
    cierreDemasDesplegables(submenu1, submenu3);
  } else if (desplegable == "submenu3") {
    let desplegable = document.getElementById("submenu3");
    toggle(desplegable);
    cierreDemasDesplegables(submenu1, submenu2);
  }
}

document.addEventListener("click", function (e) {
  if (document.getElementById("menu").contains(e.target)) {
    return;
  } else {
    submenu1.classList.remove("submenu-active");
    submenu1.classList.add("submenu-inactive");
    submenu2.classList.remove("submenu-active");
    submenu2.classList.add("submenu-inactive");
    submenu3.classList.remove("submenu-active");
    submenu3.classList.add("submenu-inactive");
  }
});

//MODO OSCURO O CLARO
let btnSwitch = document.getElementById("switch");

btnSwitch.addEventListener("change", () => {
  console.log("hola");
  document.body.classList.toggle("white-doc");

  document.body.classList.contains("white-doc")
    ? localStorage.setItem("dark-mode", "true")
    : localStorage.setItem("dark-mode", "false");
});

if (localStorage.getItem("dark-mode") === "true") {
  document.body.classList.add("white-doc");

  document.getElementById("switch").checked = true;
}
