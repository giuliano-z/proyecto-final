from django.shortcuts import render, redirect
from usuario.form import FormularioDeCreacionDeUsuarios, FormularioEditarUsuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from usuario.models import InfoExtra
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def registrarse(request):

    if request.method == 'POST':
        formulario = FormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/registro.html', {'formulario': formulario})
    formulario = FormularioDeCreacionDeUsuarios()
    return render(request, 'usuario/registro.html', {'formulario': formulario})

def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contraseña = formulario.cleaned_data['password']
            user = authenticate(username=usuario, password=contraseña)
            django_login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

@login_required
def editar_perfil(request):

    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = FormularioEditarUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            bibliografia = formulario.cleaned_data.get('bibliografia')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            if bibliografia:
                info_extra_user.bibliografia = bibliografia
                info_extra_user.save()
            formulario.save()
            return redirect('usuario:perfil')
    else:
        formulario = FormularioEditarUsuario(initial={'avatar': info_extra_user.avatar, 'bibliografia': info_extra_user.bibliografia}, instance=request.user)

    return render(request, 'usuario/editar_perfil.html', {'formulario': formulario})

@login_required
def perfil(request):
    usuario = request.user
    info_extra_usuario = InfoExtra.objects.get(user=usuario)

    return render(request, 'usuario/perfil.html', {'usuario': usuario, 'info_extra_usuario': info_extra_usuario})