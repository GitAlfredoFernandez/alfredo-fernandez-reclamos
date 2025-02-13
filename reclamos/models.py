from django.db import models
from django.contrib.auth.models import User


class Reclamo(models.Model):
    titulo = models.CharField(max_length=100)
    nombre_apellido  = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.titulo} ({self.nombre_apellido})'