#encoding:utf-8

from django.contrib.auth.models import User
from django.db import models
from empresario.storage import OverwriteStorage
from geoposition.fields import GeopositionField


class Negocio(models.Model):
	nombre = models.CharField(max_length=50)
	ubicacion = GeopositionField()
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField(max_length=10)
	imagen = models.ImageField(storage=OverwriteStorage(), upload_to='negocio', verbose_name='Imagen')
	servicios = models.CharField(max_length=20)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.nombre

class Actividades(models.Model):
	frase = models.CharField(max_length=50)
	precio = models.FloatField(max_length=10)
	evento = models.CharField(max_length=100)
	imagen = models.ImageField(storage=OverwriteStorage(), upload_to='evento', verbose_name='Imagen')
	negocio = models.ForeignKey(Negocio)

	def __unicode__(self):
		return self.frase