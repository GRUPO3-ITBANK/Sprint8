from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from Clientes.models import Cliente
from .models import MyUser
from .forms import UserCreationForm

def alta_usuario(request):
    form=UserCreationForm()
    if not (request.user.is_staff):
        return render(request, 'ITBA/index.html')
    if request.method == "POST":
        id_cliente = request.POST.get('id_cliente')
        dni = request.POST.get('dni')
        password = make_password(request.POST.get('pass'))
        cliente = Cliente.objects.filter(pk=id_cliente).first()
        MyUser(username=dni,id_cliente=cliente,password=password).save()
        return redirect(reverse('alta_usuario')+"?ok")
    return render(request, "Login/alta-usuario.html",{'form': form})
