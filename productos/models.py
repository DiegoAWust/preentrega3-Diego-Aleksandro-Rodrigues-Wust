from django.db import models
from django import forms

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    imagen=models.ImageField(upload_to="productos",null=True, blank=True)
    precio = models.IntegerField()
    disponibilidad =models.BooleanField(default=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return f"{self.nombre}"
    