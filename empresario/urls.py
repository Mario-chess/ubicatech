#encoding:utf-8

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^inicio/','empresario.views.inicio'),	
	url(r'^registro/','empresario.views.crear_empresario'),	
	url(r'^ingresar/','empresario.views.ingresar'),	
	url(r'^cerrar/','empresario.views.cerrar'),
	url(r'^principal/','empresario.views.principal'),
	url(r'^configurar/','empresario.views.configurar_perfil'),	
	url(r'^actualizar_perfil/','empresario.views.actualizar_perfil'),	
	url(r'^cambiar_password/','empresario.views.cambiar_password'),	
	)