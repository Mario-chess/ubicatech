#encoding:utf-8

# --------------------------Importaciones--------------------------
from django.db import models

from django.contrib.auth.models import User
	# Para extnder la Clase Users de Django

from empresario.storage import OverwriteStorage
	# Permite actualizar el atributo "Imagen"
	# Esto evita que el espacio del server se llene
# --------------------------------End-------------------------------


# --------------------------Atributos de clase----------------------
User.add_to_class('nombre', models.CharField(max_length=30, blank="true"))
User.add_to_class('apellido', models.CharField(max_length=30, blank="true"))
User.add_to_class('imagen', models.ImageField(storage=OverwriteStorage(), upload_to='empresario', verbose_name='Imagen'))
User.add_to_class('sexo', models.CharField(max_length=7))

# --------------------------------End-------------------------------

# Los atributos "Username", "Email",  "Password", ya están implícitos dentro de la clase "User"
