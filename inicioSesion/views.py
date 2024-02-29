from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, path
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from miapp.models import Avatar
from .forms import *
from django.views.generic import View
 
        
class register(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "inicioRegistro/registro.html",{"form":form})
    
    def post(self, request):
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.save()
            login(request, usuario)
            return redirect(reverse_lazy('inicio'))

        else:    
            messages.error(request, "Usuario no válido")
            miForm = RegistroForm()

        return render(request, "inicioRegistro/registro.html", {"form": miForm }) 




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return redirect('inicio')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
    else:
        form = AuthenticationForm()
    return render(request, "inicioRegistro/login.html", {"form": form })
    

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')