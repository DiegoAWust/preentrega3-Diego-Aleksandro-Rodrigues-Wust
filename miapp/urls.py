from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('soporte/', soporte, name="soporte"),
    path('reportes/', reporte, name="reportes"),
    path('soporte_actualizar/<id_soporte>/', updateSoporte, name="actualizarSoporte"),
    path('soporte_eliminar/<id_soporte>/', deleteSoporte, name="eliminarSoporte"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
