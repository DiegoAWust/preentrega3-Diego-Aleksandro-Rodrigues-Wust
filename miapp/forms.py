from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'email', 'contraseña', 'confirmar_contraseña']

    def clean_email(self):
        email = self.cleaned_data['email']

        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email
    
class productosForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=250, required=True)
    precio = forms.IntegerField(required=True)
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class soporteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=150, required=True)
    problematica = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = Soporte
        fields = ['nombre', 'problematica', 'email']

