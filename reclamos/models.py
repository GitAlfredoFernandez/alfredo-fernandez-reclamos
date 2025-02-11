from django.db import models


class Reclamo(models.Model):
    titulo = models.CharField(max_length=100)
    nombre_apellido  = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.titulo} ({self.nombre_apellido})'