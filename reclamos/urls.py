from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('reclamo-crear/', views.reclamo_crear, name="reclamo_crear"),
    path('reclamo-listar/', views.ReclamoListView.as_view(), name="reclamo_listar"),
    path('reclamo-detalle/<int:pk>/', views.ReclamoDetailView.as_view(), name="reclamo_detalle"),
    path('reclamo-eliminar/<int:pk>/', views.ReclamoDeleteView.as_view(), name="reclamo_eliminar"),
    path('reclamo-actualizar/<int:pk>/', views.ReclamoUpdateView.as_view(), name="reclamo_actualizar"),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='reclamos/login.html'), name='login'),
	path('salir/', views.custom_logout, name='salir'),
    path('change_profile_picture/', views.change_profile_picture, name='change_profile_picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)