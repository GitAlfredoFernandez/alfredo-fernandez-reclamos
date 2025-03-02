from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
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
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128, blank=True)
    consorcio = models.CharField(max_length=100, blank=True)
    unidad = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def save(self, *args, **kwargs):
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.email = self.email
        if self.password:
            try:
                validate_password(self.password, self.user)
                self.user.set_password(self.password)
            except ValidationError as e:
                raise ValidationError({'password': e.messages})
        self.user.save()
        super().save(*args, **kwargs)
