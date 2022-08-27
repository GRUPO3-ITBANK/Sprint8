from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Prestamo
from Cuentas.models import Cuenta
from Clientes.models import Cliente
def prestamos(request):
    if not (request.user.is_authenticated):
        return render(request, 'ITBA/index.html')
    if request.method == "POST":
        fecha_prestamo = request.POST.get('fecha_prestamo')
        tipo = request.POST.get('tipo')
        total = int(request.POST.get('total'))
        ID_cliente = Cliente.objects.filter(pk=request.user.id_cliente.id).first()
        tipo_cliente = (request.user.id_cliente.tipo_cliente).lower()

        if tipo_cliente == "classic" and total > 100000:
            return redirect(reverse('prestamos')+"?classic")
        if tipo_cliente == "gold" and total > 300000:
            return redirect(reverse('prestamos')+"?gold")
        if tipo_cliente == "black" and total > 500000:
            return redirect(reverse('prestamos')+"?black")
        else:
            Prestamo(fecha_prestamo=fecha_prestamo,tipo=tipo, total=total, ID_cliente=ID_cliente).save()

            cuenta_id_cliente = Cuenta.objects.get(ID_cliente=request.user.id_cliente.id)
            cuenta_id_cliente.balance= cuenta_id_cliente.balance + total
            cuenta_id_cliente.save()
            print(cuenta_id_cliente.balance)
        return redirect(reverse('prestamos')+"?ok")
    return render(request, 'Prestamos/prestamos.html')
