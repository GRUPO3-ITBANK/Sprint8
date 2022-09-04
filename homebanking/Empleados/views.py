from django.shortcuts import render, redirect

def home_empleado(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/home-empleado.html")
        return render(request,'home.html')
    return redirect('index')

def prestamos_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-prestamos.html")
        return redirect('home')
    return redirect('index')
    
def sol_prestamos_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-formulario-prestamo.html")
        return redirect('home')
    return redirect('index')

def anular_prestamo(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/anular-prestamo.html")
        return redirect('home')
    return redirect('index')

def tarjetas_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-tarjetas.html")
        return redirect('home')
    return redirect('index')    

def modif_cliente(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/modif-cliente.html")
        return redirect('home')
    return redirect('index')   