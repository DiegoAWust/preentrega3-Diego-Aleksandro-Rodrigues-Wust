from django.db import models
from django import forms


class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    ultimo_login = models.DateTimeField(auto_now=True)
    esta_activa = models.BooleanField(default=True)
    contraseña = models.CharField(max_length=255)
    confirmar_contraseña = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_completo}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class Soporte(models.Model):
    nombre = models.CharField(max_length=150)
    problematica = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"