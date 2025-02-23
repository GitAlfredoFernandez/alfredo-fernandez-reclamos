from django import forms
from .models import ReclamoTipo, ReclamoEstado, Profile
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ReclamoCrear(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    reclamo_tipo = forms.ModelChoiceField(
        queryset=ReclamoTipo.objects.filter(activo=True),
        empty_label="Seleccione un tipo de reclamo..."
    )
    reclamo_estado = forms.ModelChoiceField(
        queryset=ReclamoEstado.objects.filter(activo=True),
        empty_label="Seleccione un estado..."
    )

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        
class CustomLogoutForm(forms.Form):
    model = User
    fields = []