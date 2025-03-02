from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from reclamos.models import Reclamo, ReclamoEstado, ReclamoTipo, GaleriaFotos
from reclamos.forms import ReclamoCrear, UserRegisterForm, ProfileForm, CustomLogoutForm, GaleriaFotosForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'reclamos/inicio.html')

@login_required
def reclamo_crear(request, instance=None):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_classes'] = 'container d-flex flex-column align-items-center justify-content-center min-vh-100 text-center'
        return context


class ReclamoDeleteView(DeleteView):
    model = Reclamo
    template_name = 'reclamos/reclamo-eliminar.html'
    context_object_name = 'reclamo'
    success_url = reverse_lazy('reclamo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_classes'] = 'container d-flex flex-column align-items-center justify-content-center min-vh-100 text-center'
        return context


class ReclamoUpdateView(UpdateView):
    model = Reclamo
    template_name = 'reclamos/reclamo-actualizar.html'
    context_object_name = 'reclamo'
    fields = ['titulo', 'descripcion', 'reclamo_tipo', 'reclamo_estado']
    success_url = reverse_lazy('reclamo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_classes'] = 'container d-flex flex-column align-items-center justify-content-center min-vh-100 text-center'
        return context


class ReclamoListView(LoginRequiredMixin, ListView):
    model = Reclamo
    template_name = 'reclamos/reclamo-listar.html'
    context_object_name = 'reclamos'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("q", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda, autor=self.request.user)
        else:
            queryset = queryset.filter(autor=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bootstrap_classes'] = 'container d-flex flex-column align-items-center justify-content-center min-vh-100 text-center'
        return context
    
def about(request):
    return render(request, 'reclamos/about.html')

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
            try:
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado.')
                return redirect('login')
            except ValidationError as e:
                form.add_error(None, e)
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

@login_required
def galeria_fotos_upload(request, reclamo_id):
    reclamo = get_object_or_404(Reclamo, id=reclamo_id)
    if request.method == 'POST':
        form = GaleriaFotosForm(request.POST, request.FILES)
        if form.is_valid():
            galeria_foto = form.save(commit=False)
            galeria_foto.reclamo = reclamo
            galeria_foto.save()
            messages.success(request, 'Foto subida exitosamente.')
            return redirect('galeria_fotos', reclamo_id=reclamo_id)
    else:
        form = GaleriaFotosForm()
    return render(request, 'reclamos/galeria_fotos_upload.html', {'form': form, 'reclamo': reclamo})

@login_required
def galeria_fotos(request, reclamo_id):
    reclamo = get_object_or_404(Reclamo, id=reclamo_id)
    fotos = reclamo.fotos.all()
    return render(request, 'reclamos/galeria_fotos.html', {'reclamo': reclamo, 'fotos': fotos})