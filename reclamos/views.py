from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from reclamos.models import Reclamo, ReclamoEstado, ReclamoTipo
from reclamos.forms import ReclamoCrear, UserRegisterForm, ProfileForm,CustomLogoutForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'reclamos/inicio.html')


def reclamo_crear(request,instance=None):
    # print(request.GET)
    # print(request.POST)
    current_user = get_object_or_404(User, pk=request.user.pk)
    formulario = ReclamoCrear()
    if request.method == "POST":
        formulario = ReclamoCrear(request.POST)
        if formulario.is_valid():
            print('Cleaned Data:', formulario.cleaned_data)
            reclamo = Reclamo(
                titulo=formulario.cleaned_data.get('titulo'),
                descripcion=formulario.cleaned_data.get('descripcion'),
                reclamo_tipo=formulario.cleaned_data.get('reclamo_tipo'),
                reclamo_estado=formulario.cleaned_data.get('reclamo_estado'),
                autor=current_user
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
    
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('reclamo_listar')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'reclamos/register.html', context)

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
	else:
		user = current_user
        

	return render(request, 'reclamos/profile.html', {'user':user})

def change_profile_picture(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('profile')  
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'reclamos/change_profile_picture.html', context)

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('inicio')
    else:
        form = CustomLogoutForm()
    context = {'form': form}
    return render(request, 'reclamos/logout.html', context)

    return redirect('inicio') 