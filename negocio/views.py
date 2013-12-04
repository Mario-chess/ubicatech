#encoding:utf-8

# --------------------------Importaciones----------------------------------

from negocio.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from negocio.forms import *
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

# -----------------------------------------------------------------------------


# **************************Crear Empresario**************************************
@login_required(login_url='/ingresar')
def crear_negocio(request):
    if request.method=='POST':
        formulario = CrearNegocio(request.POST, request.FILES)
        if formulario.is_valid():
        	# Las tres lineas siguientes permiten obtener por defecto el valor de usuario
			negocio = formulario.save(commit=False) 
			negocio.usuario = request.user
			negocio.save()
			return HttpResponseRedirect('/principal/')
    else:
        formulario = CrearNegocio()
    return render_to_response('negocio/registro_negocio.html',{'formulario':formulario}, context_instance=RequestContext(request))

# **************************----End----***************************************

# **************************Menú Negocios**************************************
@login_required(login_url='/ingresar')
def menu_negocio (request):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	negocio = Negocio.objects.filter(usuario=user_id)
	f = User.objects.get(pk=user_id)
	return render_to_response('negocio/menu_negocio.html', {'negocio':negocio, 'datos':f} , context_instance=RequestContext(request))
# **************************End**************************************************

# **************************Menú Negocios**************************************
@login_required(login_url='/ingresar')
def configurar_negocio (request, id_negocio):
	user = request.user
	user_id=user.pk # Para mandar los datos del Usuario
	f = User.objects.get(pk=user_id) # En forma de formulario		
	return render_to_response('negocio/configurar_negocio.html', {'negocio':id_negocio, 'datos':f} , context_instance=RequestContext(request))
# **************************End**************************************************


# **************************Actualizar Empresario**************************************
@login_required(login_url='/ingresar')
def actualizar_negocio(request, id_negocio):
	user = request.user	
	user_id=user.pk
	f = Negocio.objects.get(pk=id_negocio, usuario=user_id) # Un poco de seguridad
	if request.method=='POST':
		formulario = CrearNegocio(request.POST, request.FILES, instance=f)
		if formulario.is_valid():        	
			formulario.save()
			return HttpResponseRedirect('/principal/')
	else:
		formulario = CrearNegocio(instance=f)
	return render_to_response('negocio/actualizar_negocio.html',{'formulario':formulario}, context_instance=RequestContext(request))
# **************************----End----***************************************

# **************************Crear Empresario**************************************
from django.core.urlresolvers import reverse

@login_required(login_url='/ingresar')
def agregar_evento(request, id_negocio):
    if request.method=='POST':
        formulario = CrearEvento(request.POST, request.FILES)
        if formulario.is_valid():
        	# Las tres lineas siguientes permiten obtener por defecto el valor de usuario
			actividad = formulario.save(commit=False) 
			actividad.negocio = Negocio.objects.get(pk=id_negocio)
			actividad.save()
			return HttpResponseRedirect('/principal/')

    else:
        formulario = CrearEvento()
    return render_to_response('negocio/agregar_evento.html',{'formulario':formulario}, context_instance=RequestContext(request))
# **************************----End----***************************************

