from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('reclamo-crear/', views.reclamo_crear, name="reclamo_crear"),
    path('reclamo-listar/', views.ReclamoListView.as_view(), name="reclamo_listar"),
    path('reclamo-detalle/<int:pk>/', views.ReclamoDetailView.as_view(), name="reclamo_detalle"),
    path('reclamo-eliminar/<int:pk>/', views.ReclamoDeleteView.as_view(), name="reclamo_eliminar"),
    path('reclamo-actualizar/<int:pk>/', views.ReclamoUpdateView.as_view(), name="reclamo_actualizar"),
]