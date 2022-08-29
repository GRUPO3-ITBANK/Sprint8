from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from Clientes.models import Cliente
from Empleados.models import Empleado
from .models import MyUser

def alta_user(request):
    if not (request.user.is_staff):
        return render(request, 'ITBA/index.html')
    return render(request, "Login/alta-user.html",)

    
def alta_user_cl(request):

    if not (request.user.is_staff):
        return render(request, 'ITBA/index.html')
    if request.method == "POST":
        id_cliente = request.POST.get('id_cliente')
        dni = request.POST.get('dni')
        password = make_password(request.POST.get('pass'))
        cliente = Cliente.objects.filter(pk=id_cliente).first()
        MyUser(username=dni,id_cliente=cliente,password=password).save()
        return redirect(reverse('alta-user-cl')+"?ok")
    return render(request, "Login/alta-user-cl.html")


def alta_user_empl(request):
    if not (request.user.is_staff):
        return render(request, 'ITBA/index.html')
    if request.method == "POST":
        id_empleado = request.POST.get('id_empleado')
        dni = request.POST.get('dni')
        password = make_password(request.POST.get('pass'))
        empleado = Empleado.objects.filter(pk=id_empleado).first()
        MyUser(username=dni,id_empleado=empleado,password=password).save()
        return redirect(reverse('alta-user-empl')+"?ok")
    return render(request, "Login/alta-user-empl.html")
