from django import forms
from .models import *

class productosForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=250, required=True)
    precio = forms.IntegerField(required=True)
    imagen = forms.ImageField(required=True)
    disponibilidad =forms.BooleanField(required=True)
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'disponibilidad']