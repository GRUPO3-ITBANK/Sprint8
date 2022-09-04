from django.urls import path
from .views import ClienteList, ClienteDetails, CuentaList, CuentaDetails, PrestamoList, PrestamoDetails, TarjetaList, TarjetaDetails, SucursalesList


urlpatterns = [
    path('clientes/',ClienteList.as_view()),
    path('clientes/<int:pk>/',ClienteDetails.as_view()),
    path('cuentas/',CuentaList.as_view()),
    path('cuentas/<int:pk>/',CuentaDetails.as_view()),
    path('prestamos/',PrestamoList.as_view()),
    path('prestamos/<int:pk>/',PrestamoDetails.as_view()),
    path('tarjetas/', TarjetaList.as_view()),
    path('tarjetas/<int:pk>/', TarjetaDetails.as_view()),
    path('sucursales/', SucursalesList.as_view()),
 ]


