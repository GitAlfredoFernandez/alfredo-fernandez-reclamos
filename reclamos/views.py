from django.shortcuts import render, redirect
from django.http import HttpResponse
from reclamos.models import Reclamo
from reclamos.forms import ReclamoCrear

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
                nombre_apellido=formulario.cleaned_data.get('nombre_apellido'),
                descripcion=formulario.cleaned_data.get('descripcion')
            )
            reclamo.save()
            return redirect("reclamo_listar")
            
    return render(request, 'reclamos/reclamo-crear.html', {'formulario': formulario})

def reclamo_listar(request):
    busqueda = request.GET.get('q',None)
    if busqueda:
        reclamos = Reclamo.objects.filter(titulo__icontains=busqueda)
    else:
        reclamos = Reclamo.objects.all()
    return render(request, 'reclamos/reclamo-listar.html', context={'reclamos': reclamos})