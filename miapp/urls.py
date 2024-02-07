from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('productos/', productos, name="productos"),
    path('productospopulares/', productos1, name="productos1"),
    path('nuevosproductos/', productos2, name="productos2"),
    path('registro/', registro, name="registro"),
    path('Agregarproductos/', agregar_productos, name="agregarP1"),
    path('buscar/', buscar, name="buscarP1"),
    path('buscarproductos/', buscarProductos, name="buscarProductos"),
    path('soporte/', soporte, name="soporte"),
    path('reportes/', reporte, name="reportes"),

]
