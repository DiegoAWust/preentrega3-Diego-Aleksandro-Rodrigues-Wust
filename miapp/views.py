from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.template.context_processors import csrf
from .forms import *


def inicio(request):
    return render(request, "miapp/home.html")


def nosotros(request):
    return render(request, "miapp/nosotros.html")


def productos(request):
    productos = Producto.objects.all()
    return render(request, "miapp/productos.html", {"productos": productos})


def productos1(request):
    return render(request, "miapp/productosPopulares.html")


def productos2(request):
    return render(request, "miapp/nuevosProductos.html")

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            contraseña = form.cleaned_data['contraseña']
            confirmar_contraseña = form.cleaned_data['confirmar_contraseña']

            if contraseña == confirmar_contraseña:
                form.save()
                return redirect('inicio')  
            else:
                form.add_error('confirmar_contraseña', 'Las contraseñas no coinciden.')
    else:
        form = UsuarioForm()

    return render(request, 'miapp/registro.html', {'form': form})

def agregar_productos(request):
    if request.method == "POST":
        miForm = productosForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_desc = miForm.cleaned_data.get("descripcion")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre=producto_nombre, descripcion=producto_desc, precio=producto_precio)
            producto.save()
            return redirect('productos')

    else:    
        miForm = productosForm() 

    return render(request, "miapp/agregarProductos.html", {"form": miForm })

def buscar(request):
    return render(request, "miapp/buscar.html")

def buscarProductos(request):
    buscar_param = request.GET.get("buscarP1")
    if buscar_param:
        productos = Producto.objects.filter(nombre__icontains=buscar_param)
        contexto = {"productos": productos}
        return render(request, "miapp/productos.html", contexto)
    else:
        return HttpResponse("No se ingresaron patrones de búsqueda")

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