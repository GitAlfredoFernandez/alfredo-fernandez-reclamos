from django import forms
from .models import ReclamoTipo, ReclamoEstado

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
