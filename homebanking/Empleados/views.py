from django.shortcuts import render

def home_empleado(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/home-empleado.html")
        return render(request,"ITBA/home.html")
    return render(request, 'ITBA/index.html')

def prestamos_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-prestamos.html")
        return render(request,"ITBA/home.html")
    return render(request, 'ITBA/index.html')
    
def sol_prestamos_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-formulario-prestamo.html")
        return render(request,"ITBA/home.html")
    return render(request, 'ITBA/index.html')

def tarjetas_empl(request):
    if request.user.is_authenticated:
        if (request.user.id_empleado is not None):
            return render(request, "Empleados/empl-tarjetas.html")
        return render(request,"ITBA/home.html")
    return render(request, 'ITBA/index.html')    