#encoding:utf-8

# -----------------------------------------------------------------------------

from django.forms import ModelForm
from django import forms
from empresario.models import *
from django.contrib.auth.models import User

# -----------------------------------------------------------------------------

SEXO = (('Hombre', 'Hombre'),('Mujer', 'Mujer'))

# **************************Crear Empresario**************************************

from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# **************************----End----***************************************


# **************************Editar Empresario**************************************

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

class EditarEmpresario(ModelForm):

	username = forms.CharField(label="Nombre de Usuario")
	nombre = forms.CharField(label="Nombre")
	apellido = forms.CharField(label="Apellido")
	sexo = forms.ChoiceField(label="Sexo",  choices=SEXO)
	email = forms.CharField(label="Correo Electrónico")
	# fotografia = forms.ImageField(label="Imagen")
	imagen= ImageField50KB(widget=forms.FileInput)
	class Meta:
		model = User
		fields = ('username', 'nombre', 'apellido', 'sexo', 'email', 'imagen')
		

# **************************----End----***************************************

