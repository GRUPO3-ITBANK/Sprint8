# Sprint7

## Introducción

ITBANK ha trabajando desde el principio en la creación del front-end web para los clientes del banco, luego se dedicó al back-end generando un modelo y base de datos para almacenar la información. El objetivo es unir el front-end con el back-end. De la misma forma que un diseñador de autos no puede crear el motor del mismo sin tener alguna referencia sobre cómo será la carrocería en sí, no se puede crear un back-end sin tener una referencia sobre cómo será el front-end. Por eso trabajamos en la siguiente modalidad: El equipo de desarrollo definió como estándar de trabajo el framework DJANGO.

---

## Primera problemática

Se requiere crear el proyecto DJANGO homebanking, el mismo estará compuesto por las siguientes apps:

- Clientes
- Cuentas
- Tarjetas
- Prestamos
- Login

A partir de la base de datos trabajada en el sprint 6, se requiere crear un modelo dentro de DJANGO con las siguientes tablas:

- Cliente
- Cuenta
- Empleado
- Movimientos
- Prestamos
- Tarjeta

Para tal fin usar el comando inspectdb (https://docs.djangoproject.com/en/4.0/howto/legacy-databases/)

- Adaptar los siguientes templates generados en el frontend dentro de django agregando los templates tags necesarios para su utilización. Se deben incluir los recursos estáticos utilizados en el diseño del sitio.
  Crear las vistas que interactúen con los templates y el modelo

---

## Segunda problemática

Incorporar el registro y autenticación de clientes para todo el sitio. Se debe utilizar el sistema de autenticación provisto por DJANGO.
Se necesita generar una relación entre el usuario que se autentica y la información de cliente almacenada. Debería haber una relación 1 a 1 entre cliente y usuario.
Se debe agregar al menú del home banking la opción de salir o cerrar sesión
Una vez autenticado el usuario, el home banking debe mostrar su nombre en algún lugar del sitio.
Todas las páginas del sitio tienen que chequear que el usuario esta autenticado.

---

## Tercera problemática

Crear un formulario de solicitud de préstamos pre-aprobados dentro del home banking. El formulario deberá ser enviado por POST y tener protección contra Cross site request forgery.
Entendiendo que el cliente se autentico en el sitio, podemos obtener los datos de cliente para hacer validaciones.
El cliente debe poder elegir el tipo de préstamo y la fecha de inicio. El monto de pre aprobación depende del tipo de cliente con los siguientes límites: BLACK 500000$, GOLD 300000$ y CLASSIC 100000$
Una vez solicitado debe registrarse en la base de datos la solicitud, impactando en préstamo y en el saldo de cuenta.
En todo momento el formulario informará si la solicitud fue aprobada o rechazada.

---

Superusuario: 9000
Contraseña: 9000

Usuario comun: 120
Contraseña: 120