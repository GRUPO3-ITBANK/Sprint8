from django.urls import path
from Empleados import views

urlpatterns = [
    path('home/', views.home_empleado, name="home-empleado"),
    path('prestamos/', views.prestamos_empl, name="prestamos-empl"),
    path('solicitar-prestamo/', views.sol_prestamos_empl, name="sol-prestamos-empl"),
    path('anular-prestamo/', views.anular_prestamo, name="anular-prestamo"),
    path('tarjetas/', views.tarjetas_empl, name="tarjetas-empl"),
    path('modificar-cliente/', views.modif_cliente, name="modif-cliente"),
 ]


