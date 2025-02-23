from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
import os

class ReclamoTipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    @classmethod
    def get_default_pk(cls):
        tipo, _ = cls.objects.get_or_create(
            nombre='General',
            defaults={'descripcion': 'Reclamos generales'}
        )
        return tipo.pk

class ReclamoEstado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    @classmethod
    def get_default_pk(cls):
        estado, _ = cls.objects.get_or_create(
            nombre='Nuevo',
            defaults={'descripcion': 'Reclamo recién creado'}
        )
        return estado.pk
    
class Reclamo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    reclamo_estado = models.ForeignKey(ReclamoEstado, on_delete=models.PROTECT, null=False, default=ReclamoEstado.get_default_pk)
    reclamo_tipo = models.ForeignKey(ReclamoTipo, on_delete=models.PROTECT, null=False, default=ReclamoTipo.get_default_pk) 
    
    def __str__(self):
        return f'{self.titulo} ({self.reclamo_estado.nombre})'
    
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='defaultuser.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'
