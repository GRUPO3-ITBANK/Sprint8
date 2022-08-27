from django.shortcuts import render
from Cuentas.models import Cuenta
# Create your views here.

def init(request):
    if request.user.is_authenticated:
        return render(request, "ITBA/home.html")
    else:
        return render(request, "ITBA/index.html")

def index(request):
    return render(request, "ITBA/index.html")

def home(request):
    if request.user.is_authenticated:
        totalCajaAhorro= Cuenta.objects.get(ID_cliente=request.user.id_cliente.id).balance
        return render(request, "ITBA/home.html",{"totalCajaAhorro":totalCajaAhorro})
        
    else:
        return render(request, "ITBA/index.html")

