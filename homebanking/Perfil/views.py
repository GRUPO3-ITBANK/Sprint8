from django.shortcuts import render

def perfil(request):
    if request.user.is_authenticated:
        if not (request.user.is_staff):
            return render(request, "Perfil/perfil.html")
        else:
            return render(request, "Perfil/perfil.html")
    else:
        return render(request, "ITBA/index.html")