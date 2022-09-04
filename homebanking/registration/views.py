from django.shortcuts import redirect, render
from django.urls import re_path


# Create your views here.
def profile(request):
    return render(request,"registration/profile.html")

def logout(request):
    if request.user.is_authenticated:
        return render(request,"registration/logout.html")
    return redirect('index')