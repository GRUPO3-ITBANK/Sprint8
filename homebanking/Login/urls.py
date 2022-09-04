from django.urls import path
from Login import views

urlpatterns = [
    path('home/', views.home_super_user, name="home-superuser"),
    path('alta-user/', views.alta_user, name="alta-user"),
    path('alta-user-cliente/', views.alta_user_cl, name="alta-user-cl"),
    path('alta-user-empleado/', views.alta_user_empl, name="alta-user-empl"),
 ]


