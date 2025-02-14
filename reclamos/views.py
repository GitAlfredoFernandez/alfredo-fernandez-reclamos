from django.shortcuts import render, redirect
from django.http import HttpResponse
from reclamos.models import Reclamo, ReclamoEstado, ReclamoTipo
from reclamos.forms import ReclamoCrear
from django.views.generic import ListView

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'reclamos/inicio.html')

def reclamo_crear(request):
    # print(request.GET)
    # print(request.POST)
    formulario = ReclamoCrear()
    if request.method == "POST":
        formulario = ReclamoCrear(request.POST)
        if formulario.is_valid():
            print('Cleaned Data:', formulario.cleaned_data)
            reclamo = Reclamo(
                titulo=formulario.cleaned_data.get('titulo'),
                descripcion=formulario.cleaned_data.get('descripcion'),
                reclamo_tipo=formulario.cleaned_data.get('reclamo_tipo'),
                reclamo_estado=formulario.cleaned_data.get('reclamo_estado')
            )
            reclamo.save()
            return redirect("reclamo_listar")
            
    return render(request, 'reclamos/reclamo-crear.html', {'formulario': formulario})



class ReclamoListView(ListView):
    model = Reclamo
    template_name = 'reclamos/reclamo-listar.html'
    context_object_name = 'reclamos'
    
    def get_queryset(self):
        return Reclamo.objects.select_related('reclamo_estado','reclamo_tipo')