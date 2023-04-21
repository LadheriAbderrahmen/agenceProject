from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.loginp, name="login"),
    path('registre',views.registre, name="registre"),
    path('a propos',views.propos, name="propos"),
    

]