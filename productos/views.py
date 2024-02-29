from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required

@login_required
def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {"productos": productos})

@login_required
def agregar_productos(request):
    if request.method == "POST":
        miForm = productosForm(request.POST, request.FILES)
        if miForm.is_valid():
            miForm.save()
            return redirect('productos')
    else:
        miForm = productosForm() 
    return render(request, "productos/agregarProductos.html", {"form": miForm })

@login_required
def buscar(request):
    return render(request, "productos/buscar.html")

@login_required
def buscarProductos(request):
    buscar_param = request.GET.get("buscarP1")
    if buscar_param:
        productos = Producto.objects.filter(nombre__icontains=buscar_param)
        contexto = {"productos": productos}
        return render(request, "productos/productos.html", contexto)
    else:
        return HttpResponse("No se ingresaron patrones de búsqueda")
    
@login_required
def updateProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = productosForm(request.POST, request.FILES)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get('nombre')
            producto.descripcion = miForm.cleaned_data.get('descripcion')
            producto.precio = miForm.cleaned_data.get('precio')
            producto.imagen = miForm.cleaned_data.get('imagen')
            producto.disponibilidad = miForm.cleaned_data.get('disponibilidad')
            producto.save()
            return redirect(reverse_lazy('productos'))   
    else:
        miForm = productosForm(initial={
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'imagen': producto.imagen,
            'disponibilidad': producto.disponibilidad
        })
    return render(request, "productos/actualizarProducto.html", {'form': miForm})

@login_required
def deleteProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect(reverse_lazy('productos'))