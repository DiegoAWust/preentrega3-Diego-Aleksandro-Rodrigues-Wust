from django.urls import path, include
from .views import *


urlpatterns = [
    path('productos/', productos, name="productos"),
    path('Agregarproductos/', agregar_productos, name="agregarP1"),
    path('buscar/', buscar, name="buscarP1"),
    path('buscarproductos/', buscarProductos, name="buscarProductos"),
    path('producto_actualizar/<id_producto>/', updateProducto, name="actualizarProducto"),
    path('producto_eliminar/<id_producto>/', deleteProducto, name="eliminarProducto"),
]