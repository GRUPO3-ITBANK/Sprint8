"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import registration, ITBA,  Prestamos, Login
from Login import views
from Prestamos import views
from ITBA import views
from registration import views

urlpatterns = [
    path('home/', ITBA.views.home, name="home"),
    path('', ITBA.views.init, name="init"),
    path('index/', ITBA.views.index, name="index"),
    path('admin/', admin.site.urls),
    path('logout-session/', registration.views.logout, name='logout-session'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('prestamos/', Prestamos.views.prestamos, name="prestamos"),
    path('alta-usuario/', Login.views.alta_usuario, name="alta_usuario"),
]
