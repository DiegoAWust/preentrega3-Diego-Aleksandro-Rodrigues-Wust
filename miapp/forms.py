from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class soporteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=150, required=True)
    problematica = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = Soporte
        fields = ['nombre', 'problematica', 'email']

#_______________________________editar usuario_______________________________#

class UserEditForm(UserCreationForm):
    username = forms.CharField(max_length=70, required=True)
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username' ,'email', 'password1', 'password2']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)