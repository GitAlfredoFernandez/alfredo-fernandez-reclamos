from django import forms
from .models import ReclamoTipo, ReclamoEstado, Profile
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ReclamoCrear(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    reclamo_tipo = forms.ModelChoiceField(
        queryset=ReclamoTipo.objects.filter(activo=True),
        empty_label="Seleccione un tipo de reclamo..."
    )
    reclamo_estado = forms.ModelChoiceField(
        queryset=ReclamoEstado.objects.filter(activo=True),
        empty_label="Seleccione un estado..."
    )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name  = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
        help_texts = {k:"" for k in fields }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
  
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name  = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Imagen de perfil', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'telefono', 'password', 'password2','image']
        help_texts = {k:"" for k in fields }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        
class CustomLogoutForm(forms.Form):
    model = User
    fields = []