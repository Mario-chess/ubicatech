#encoding:utf-8

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^crear_negocio/','negocio.views.crear_negocio'),	
	url(r'^configurar_negocio/(?P<id_negocio>\d+)$','negocio.views.configurar_negocio'),
	url(r'^actualizar_negocio/(?P<id_negocio>\d+)$','negocio.views.actualizar_negocio'),
	url(r'^agregar_evento/(?P<id_negocio>\d+)$','negocio.views.agregar_evento', name="evento"),	
	url(r'^menu_negocio/','negocio.views.menu_negocio'),	
	)