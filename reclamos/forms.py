from django import forms

class ReclamoCrear(forms.Form):
    titulo = forms.CharField(max_length=100)
    nombre_apellido = forms.CharField(max_length=20)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)