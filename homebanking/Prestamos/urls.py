from django.urls import path
from Prestamos import views

urlpatterns = [
    path('solicitar-prestamo/', views.solicitud_prestamo, name="solicitud-prestamo"),
    path('', views.prestamos, name="prestamos"),
 ]


