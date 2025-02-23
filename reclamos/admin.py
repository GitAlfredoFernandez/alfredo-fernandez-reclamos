from django.contrib import admin
from .models import Reclamo, ReclamoEstado, ReclamoTipo, Profile

@admin.register(Reclamo)
class ReclamoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'autor']
    search_fields = ['titulo', 'descripcion']
    ordering = ['-fecha']
    raw_id_fields = ['autor']

admin.site.register(ReclamoEstado)
admin.site.register(ReclamoTipo)

admin.site.register(Profile)
