let movimientos = [];
let cuentas = [];
let tarjetas = [];

width = document.documentElement.clientWidth;
height = document.documentElement.clientHeight;
//chequeo si la lista aun no tiene objetos
if (movimientos.length == 0) {
  //div contenedor donde se pushean todos los movimientos
  let contenedor = document.getElementById("cuerpoMovimientos");
  let tr = document.createElement("tr");
  tr.setAttribute("id", "movimientoConformado");
  tr.classList = "text-center";
  let td = document.createElement("td");
  td.textContent = "Todavía no has realizado ningún movimiento... :)";
  tr.append(td);
  contenedor.append(tr);
}

function generarNumeroRandom() {
  return Math.random() * (1000 - 100) + 100;
}

function agregarMov() {
  //fixx de altura

  if (document.getElementById("padre-ultimosmovimientos").clientHeight > 600) {
    document
      .getElementById("main-contenedor")
      .setAttribute(
        "style",
        "background: var(--gradient); height:max-content;"
      );
  }
  //creacion de nuevo objeto
  let objetoMovimiento = new Object();

  //creo un numero random para hardcoedar un numero de operacion al objeto
  function nOperacion(lista) {
    if (lista.length > 0) {
      for (x in lista) {
        let nRandom = generarNumeroRandom();
        if (x.nOperacion != nRandom) {
          return nRandom;
        }
      }
    } else return generarNumeroRandom();
  }

  //asigno datos hardcodeados a cada propiedad del objeto
  objetoMovimiento.nOperacion = nOperacion(movimientos);
  objetoMovimiento.tipoDeMovimiento = prompt("TIPO DE MOVIMIENTO SE REALIZÓ");
  objetoMovimiento.gasto = prompt("CUANTO GASTO");
  objetoMovimiento.metodo = prompt("Ingrese con qué pagó");
  objetoMovimiento.destino = prompt("DONDE O A QUIEN SE LE PAGÓ");
  objetoMovimiento.fecha = new Date().toLocaleString();

  let tr = document.createElement("tr");
  tr.setAttribute("id", "movimientoConformado");

  tr.setAttribute(
    "onclick",
    "mostrar('overlay');datosDelOverlay('" +
      objetoMovimiento.nOperacion +
      "','" +
      objetoMovimiento.tipoDeMovimiento +
      "','" +
      objetoMovimiento.gasto +
      "','" +
      objetoMovimiento.metodo +
      "','" +
      objetoMovimiento.destino +
      "','" +
      objetoMovimiento.fecha +
      "')"
  );

  movimientos.push(objetoMovimiento);

  contenedor = document.getElementById("cuerpoMovimientos");
  let td = document.createElement("td");
  let divInfo = document.createElement("div");
  divInfo.classList = "d-flex justify-content-between";
  let divFecha = document.createElement("div");
  let divTipoMovimiento = document.createElement("div");
  divTipoMovimiento.classList = "fw-semibold";
  let divMonto = document.createElement("div");

  divFecha.textContent = objetoMovimiento.fecha;
  divTipoMovimiento = objetoMovimiento.tipoDeMovimiento;
  divMonto.textContent = "$ " + objetoMovimiento.gasto;

  divInfo.append(divTipoMovimiento, divMonto);
  td.append(divFecha, divInfo);
  tr.append(td);
  if (movimientos.length == 1) {
    let trAux = document.createElement("tr");
    trAux.append(tr);
    contenedor.innerHTML = trAux.innerHTML;
  } else if (movimientos.length > 1) {
    contenedor.prepend(tr);
  }
}

function ocultar(id) {
  let elemento = document.getElementById(id);
  elemento.style.display = "none";
  elemento.style.visibility = "hidden";
}
function mostrar(id) {
  let elemento = document.getElementById(id);
  elemento.style.display = "flex";
  elemento.style.visibility = "visible";
}

function datosDelOverlay(nOp, tipoMovimiento, valor, metodo, destino, fecha) {
  let titulo = document.getElementById("tituloModal");
  titulo.textContent = "n° de operación: " + nOp;
  let body = document.getElementById("detalleOperacion");
  body.innerHTML =
    tipoMovimiento +
    " a: " +
    destino +
    "<br />" +
    "Monto: $" +
    valor +
    "<br />" +
    "Pagaste con: " +
    metodo +
    "<br />" +
    fecha;
}

document.addEventListener(
  "click",
  function (event) {
    if (
      !event.target.closest("#overlayHijo") &&
      !event.target.closest("#movimientoConformado")
    ) {
      ocultar("overlay");
    }
  },
  false
);
