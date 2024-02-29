from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', cerrarSesion, name="cerrarSesion"),
    path('registro/', register.as_view(), name="registro"),

]