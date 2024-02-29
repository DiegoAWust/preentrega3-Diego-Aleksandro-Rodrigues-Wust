from django.db import models
from django import forms
from django.contrib.auth.models import User


class Soporte(models.Model):
    nombre = models.CharField(max_length=150)
    problematica = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"