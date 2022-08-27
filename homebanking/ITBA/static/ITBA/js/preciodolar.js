function traerDatosDolar() {
  fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then((resp) => resp.json()) //recibo objeto de la request y lo convierto en objeto json
    .then(function (data) {
      //proceso json
      let list = data;
      console.log(data);
      //   console.log(list[1].casa);

      for (let c of list) {
        if (parseInt(c.casa.venta) > 0 && parseInt(c.casa.compra) > 0) {
          let contenedor = document.getElementById("apartadoDolar");
          let ul = document.createElement("ul");
          ul.classList =
            "ul-dolar col-12 col-lg-3 p-2 bg-white bg-opacity-10 rounded text-center m-3";
          let liNombre = document.createElement("li");
          liNombre.classList =
            "fw-bolder text-uppercase mb-1 bg-dark bg-opacity-10 rounded";
          let liVenta = document.createElement("li");
          let liCompra = document.createElement("li");
          liNombre.textContent = c.casa.nombre;
          liVenta.textContent = "VENTA: $" + c.casa.venta;
          liCompra.textContent = "COMPRA: $" + c.casa.compra;

          ul.append(liNombre);
          ul.append(liVenta);
          ul.append(liCompra);

          contenedor.append(ul);
        }
      }
    });
}

traerDatosDolar();
