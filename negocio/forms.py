#encoding:utf-8

# -----------------------------------------------------------------------------

from django.forms import ModelForm
from django import forms
from negocio.models import *
from django.contrib.auth.models import User

# -----------------------------------------------------------------------------

SERVICIOS = (('Restaurante', 'Restaurante'),('Discoteca', 'Discoteca'))

class ImageField50KB(forms.ImageField):
    # Esta es una clase que restringe el tamaño de la imagen
    def __init__(self, *args, **kwargs):
        super(ImageField50KB, self).__init__(*args, **kwargs)

        self.label = (u'Imagen')

        self.helptext = (u'Attach a current passport photograph')

    def clean(self, data, initial):
        if not data and initial:
            return initial
        f = super(ImageField50KB, self).clean(data)

        if not (f.size <= 500000):
             raise forms.ValidationError((u'Image is too large, Maximum filesize allowed is 50kB' ))
        return f

# **************************Crear Empresario**************************************
class CrearNegocio(ModelForm):
    servicios = forms.ChoiceField(label="Actividad",  choices=SERVICIOS)
    imagen= ImageField50KB(widget=forms.FileInput)

    class Meta:
        model = Negocio
        fields = ("nombre", "ubicacion", "direccion", "telefono", "imagen", "servicios")  
# **************************----End----***************************************

# **************************Crear Evento**************************************
class CrearEvento(ModelForm):
    imagen= ImageField50KB(widget=forms.FileInput)
    class Meta:
        model = Actividades
        exclude = ("negocio")  
# **************************----End----***************************************

