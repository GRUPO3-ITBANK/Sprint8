![image](https://user-images.githubusercontent.com/29070543/187229726-30dc4bf7-4cde-4954-b0b6-272454f8a645.png)



# Sprint 8

## Procesamiento Batch de Cheques

---------------
Problematica
------------
En ITBANK se piensa en facilitar en todo momento la operación de nuestros clientes, por ese motivo, se necesita contar con una API REST que contengauna serie de servicios que permita interactuar con el banco de forma autónoma para nuestros clientes.
La API que vamos a desarrollar es privada, accesible sólo a usuarios registrados e identificados por el banco. En este caso usaremos, BasicAuthentication para generar una clave que permita al usuario interactuar con nuestros servicios. Solo un usuario cliente puede consultar sus propios datos. Los servicios a generar que puedan ser utilizados por los clientes son los siguientes:
- OBTENER DATOS DE UN CLIENTE: Un cliente autenticado puede consultar sus propios datos.
- OBTENER SALDO DE CUENTA DE UN CLIENTE: Un cliente autenticado puede obtener el tipo de cuenta y su saldo.
- OBTENER MONTO DE PRESTAMOS DE UN CLIENTE: Un cliente autenticado puede obtener el tipo de préstamo y total del mismo.
- OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL: Un empleado autenticado puede obtener el listado de préstamos otorgados de una sucursal determinada.
- OBTENER TARJETAS ASOCIADAS A UN CLIENTE: Un empleado autenticado puede obtener el listado de tarjetas de crédito de un cliente determinado.
- GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE: Un empleado autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta.
- ANULAR SOLICITUD DE PRESTAMO DE CLIENTE: Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo el monto correspondiente.
- MODIFICAR DIRECCION DE UN CLIENTE: El propio cliente autenticado o un empleado puede modificar las direcciones.
- LISTADO DE TODAS LAS SUCURSALES: Un endpoint público que devuelve el listado todas las sucursales con la información correspondiente

Superusuario: 9000 clave: 9000. Usuario cliente de pruebas: 120 clave 120. Usuario empleado de pruebas: 200 clave 200
