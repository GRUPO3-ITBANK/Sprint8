from django.shortcuts import render, redirect

def perfil(request):
    if request.user.is_authenticated:
        if request.user.is_staff or  not (request.user.id_empleado_id == None): #si es staff o empleado no tienen perfil..
                return redirect("home")
        return render(request, "Perfil/perfil.html")
    else:
        return redirect('index')

