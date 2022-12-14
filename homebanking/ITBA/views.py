from django.shortcuts import render, redirect
from Cuentas.models import Cuenta
# Create your views here.

def init(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect ("home-superuser")
        if not (request.user.id_empleado_id == None):
            return redirect("home-empleado")
        return redirect('home')
    else:
        return redirect('index')

def index(request):
    return render(request, "ITBA/index.html")

def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, "Login/home-superuser.html")
        if not (request.user.id_empleado_id == None):
            return render(request, "Empleados/home-empleado.html")
        return render(request, "ITBA/home.html")
    else:
        return redirect('index')

def sucursales(request):
    return render(request, "ITBA/sucursales.html")
