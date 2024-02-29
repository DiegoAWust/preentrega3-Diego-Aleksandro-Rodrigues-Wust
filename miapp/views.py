from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.middleware.csrf import get_token
from django.template.context_processors import csrf

from carrito.carro import Carro
from .forms import *


from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


def inicio(request):

    carro=Carro(request)

    return render(request, "miapp/home.html")

@login_required
def nosotros(request):
    return render(request, "miapp/nosotros.html")

#_______________________________soporte_______________________________#

@login_required
def soporte(request):
    if request.method == "POST":
        miForm = soporteForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect('home')
    else:
        miForm = soporteForm()

    reportes = Soporte.objects.all()
    return render(request, "miapp/soporte.html", {"form": miForm, "reportes": reportes})

@login_required
def reporte(request):
    if request.method == "POST":
        miForm = soporteForm(request.POST)
        if miForm.is_valid():
            soporte_nombre = miForm.cleaned_data.get("nombre")
            soporte_problematica = miForm.cleaned_data.get("problematica")
            soporte_email = miForm.cleaned_data.get("email")
            soporte = Soporte(nombre=soporte_nombre, problematica=soporte_problematica, email=soporte_email)
            soporte.save()
            return redirect('soporte')

    else:    
        miForm = soporteForm() 

    return render(request, "miapp/reporte.html", {"form": miForm })

@login_required
def updateSoporte(request, id_soporte):
    soporte = Soporte.objects.get(id=id_soporte)
    if request.method == "POST":
        miForm = soporteForm(request.POST)
        if miForm.is_valid():
            soporte.nombre = miForm.cleaned_data.get('nombre')
            soporte.problematica = miForm.cleaned_data.get('problematica')
            soporte.email = miForm.cleaned_data.get('email')
            soporte.save()
            return redirect(reverse_lazy('soporte'))   
    else:
        miForm = soporteForm(initial={
            'nombre': soporte.nombre,
            'problematica': soporte.problematica,
            'email': soporte.email,
        })
    return render(request, "miapp/actualizarSoporte.html", {'form': miForm})

@login_required
def deleteSoporte(request, id_soporte):
    soporte = Soporte.objects.get(id=id_soporte)
    soporte.delete()
    return redirect(reverse_lazy('soporte'))

#_______________________________editar usuario_______________________________#

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.username = informacion['username']
            user.email = informacion['email']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "miapp/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "miapp/editarPerfil.html", {"form": form }) 

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "miapp/home.html")

    else:    
        form = AvatarForm()

    return render(request, "miapp/agregarAvatar.html", {"form": form })  

   