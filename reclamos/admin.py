from django.contrib import admin
from .models import Reclamo

@admin.register(Reclamo)
class ReclamoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nombre_apellido', 'fecha', 'autor']
    search_fields = ['titulo', 'nombre_apellido', 'descripcion']
    ordering = ['-fecha']
    raw_id_fields = ['autor']