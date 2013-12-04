#encoding:utf-8

# --------------------------Importaciones----------------------------------

from empresario.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from empresario.forms import *
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

# -----------------------------------------------------------------------------

# **************************Pagina de Inicio**************************************
def inicio (request):
	return render_to_response('index.html', context_instance=RequestContext(request))
# **************************End**************************************************


# **************************Crear Empresario**************************************
def crear_empresario(request):
    if request.method=='POST':
        formulario = UserCreateForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ingresar/')
    else:
        formulario = UserCreateForm()
    return render_to_response('empresario/registro_empresario.html',{'formulario':formulario}, context_instance=RequestContext(request))

# **************************----End----***************************************

# **************************Login*******************************
def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/principal/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/principal/')
                else:
                    return render_to_response('index.html', context_instance=RequestContext(request))
            else:
                return render_to_response('index.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('empresario/login.html',{'formulario':formulario}, context_instance=RequestContext(request))
# **************************----End----***************************************

# **************************LogOut*******************************
@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/inicio/')
# **************************----End----***************************************

# **************************Pagina Principal**************************************
@login_required(login_url='/ingresar')
def principal (request):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	f = User.objects.get(pk=user_id) # En forma de formulario
	return render_to_response('principal.html', {'datos':f}  ,context_instance=RequestContext(request))
# **************************End**************************************************

# **************************Pagina Principal**************************************
@login_required(login_url='/ingresar')
def configurar_perfil (request):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	f = User.objects.get(pk=user_id) # En forma de formulario
	return render_to_response('empresario/configurar_perfil.html', {'datos':f} , context_instance=RequestContext(request))
# **************************End**************************************************


# **************************Actualizar Perfil*********************************
@login_required(login_url='/ingresar')
def actualizar_perfil(request):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	f = User.objects.get(pk=user_id) # En forma de formulario
	if request.method=='POST':
		formulario = EditarEmpresario(request.POST, request.FILES, instance=f)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/configurar/')
	else:
		formulario = EditarEmpresario(instance=f)
	return render_to_response('empresario/actualizar_perfil.html',{'formulario':formulario, 'f':f}, context_instance=RequestContext(request))
# **************************----End----***************************************


# **************************Cambiar Contraseña*********************************
@login_required(login_url='/ingresar')
def cambiar_password(request):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	f = User.objects.get(pk=user_id) # En forma de formulario
	if request.method=='POST':
		formulario = PasswordChangeForm(request.user, request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/configurar/')
	else:
		formulario = PasswordChangeForm(request.user, request.POST)
	return render_to_response('empresario/cambiar_password.html',{'formulario':formulario}, context_instance=RequestContext(request))
# **************************----End----***************************************
