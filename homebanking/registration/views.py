from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,"registration/profile.html")

def logout(request):
    return render(request,"registration/logout.html")