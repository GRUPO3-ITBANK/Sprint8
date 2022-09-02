"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from API.views import ClienteList,ClienteDetails, CuentaList, PrestamoDetails, PrestamoList, TarjetaList, SucursalesList, TarjetaDetails, CuentaDetails
import registration, ITBA,  Prestamos, Login, Perfil, Empleados
from Perfil import views
from Login import views
from Prestamos import views
from ITBA import views
from registration import views
from Empleados import views

urlpatterns = [
    path('home/', ITBA.views.home, name="home"),
    path('', ITBA.views.init, name="init"),
    path('index/', ITBA.views.index, name="index"),
    path('sucursales/', ITBA.views.sucursales, name="sucursales"),
    path('admin/', admin.site.urls),

    path('logout-session/', registration.views.logout, name='logout-session'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('solicitud-prestamo/', Prestamos.views.solicitud_prestamo, name="solicitud-prestamo"),
    path('prestamos/', Prestamos.views.prestamos, name="prestamos"),

    path('home-superuser/', Login.views.home_super_user, name="home-superuser"),
    path('alta-user/', Login.views.alta_user, name="alta-user"),
    path('alta-user-cl/', Login.views.alta_user_cl, name="alta-user-cl"),
    path('alta-user-empl/', Login.views.alta_user_empl, name="alta-user-empl"),

    path('home-empleado/', Empleados.views.home_empleado, name="home-empleado"),
    path('prestamos-empl/', Empleados.views.prestamos_empl, name="prestamos-empl"),
    path('sol-prestamos-empl/', Empleados.views.sol_prestamos_empl, name="sol-prestamos-empl"),
    path('anular-prestamo/', Empleados.views.anular_prestamo, name="anular-prestamo"),
    path('tarjetas-empl/', Empleados.views.tarjetas_empl, name="tarjetas-empl"),
    path('modif-cliente/', Empleados.views.modif_cliente, name="modif-cliente"),

    path('perfil/', Perfil.views.perfil, name="perfil" ),

    path('API/clientes/',ClienteList.as_view()),
    path('API/clientes/<int:pk>/',ClienteDetails.as_view()),
    path('API/cuentas/',CuentaList.as_view()),
    path('API/cuentas/<int:pk>/',CuentaDetails.as_view()),
    path('API/prestamos/',PrestamoList.as_view()),
    path('API/prestamos/<int:pk>/',PrestamoDetails.as_view()),
    path('API/tarjetas/', TarjetaList.as_view()),
    path('API/tarjetas/<int:pk>/', TarjetaDetails.as_view()),
    path('API/sucursales/', SucursalesList.as_view()),
    
]
