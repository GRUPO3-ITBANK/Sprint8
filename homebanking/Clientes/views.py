# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.contrib.auth.hashers import make_password
# from django.http import HttpResponseRedirect
# from .models import Cliente
# # Create your views here.

# def alta_cliente(request):
#     if not (request.user.is_staff):
#         return render(request, 'ITBA/index.html')
#     if request.method == "POST":
#         dni = request.POST.get('dni','')
#         email = request.POST.get('email','')
#         nombre = request.POST.get('name','')
#         apellido = request.POST.get('last_name','')
#         fecha_de_nac = request.POST.get('dob','')
#         tipo_cliente= request.POST.get('tipo_cliente','')
#         password = make_password(request.POST.get('pass',''))
#         Cliente(DNI=dni, email=email,nombre=nombre,apellido=apellido, fecha_de_nac=fecha_de_nac,tipo_cliente=tipo_cliente, password=password).save()
#         return redirect(reverse('alta_cliente')+"?ok")
#     return render(request, "Clientes/alta-usuario.html")
