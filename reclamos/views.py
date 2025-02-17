from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from reclamos.models import Reclamo, ReclamoEstado, ReclamoTipo
from reclamos.forms import ReclamoCrear
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'reclamos/inicio.html')

def reclamo_crear(request,instance=None):
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

class ReclamoDetailView(DetailView):
    model = Reclamo
    template_name = 'reclamos/reclamo-detalle.html'
    context_object_name = 'reclamo'
    
class ReclamoDeleteView(DeleteView):
    model = Reclamo
    template_name = 'reclamos/reclamo-eliminar.html'
    context_object_name = 'reclamo'
    success_url = reverse_lazy('reclamo_listar')

class ReclamoUpdateView(UpdateView):
    model = Reclamo
    template_name = 'reclamos/reclamo-actualizar.html'
    context_object_name = 'reclamo'
    fields = ['titulo', 'descripcion', 'reclamo_tipo', 'reclamo_estado']
    success_url = reverse_lazy('reclamo_listar')
    
class ReclamoListView(ListView):
    model = Reclamo
    template_name = 'reclamos/reclamo-listar.html'
    context_object_name = 'reclamos'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("q", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset