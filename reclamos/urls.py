from django.urls import path
from reclamos.views import inicio, reclamo_crear, reclamo_listar

urlpatterns = [
    path('', inicio, name="inicio"),
    path('reclamo-crear/', reclamo_crear, name="reclamo_crear"),
    path('reclamo-listar/', reclamo_listar, name="reclamo_listar"),
]