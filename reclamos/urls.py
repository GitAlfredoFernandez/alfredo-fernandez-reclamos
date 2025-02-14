from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('reclamo-crear/', views.reclamo_crear, name="reclamo_crear"),
    path('reclamo-listar/', views.ReclamoListView.as_view(), name="reclamo_listar"),
]