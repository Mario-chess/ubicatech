#encoding:utf-8

# -------------------------Para manejar el Proyecto de manera Local----------------------------------

import os

RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

# ------------------------.Para manejar el Proyecto de manera Local----------------------------------

# Django settings for recetario_mario project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        # -------------------------------------------------------------------------------------------
        # 'NAME': '/home/mario555/ubicatech/ubicatech.db',  # Puesta en Producción        
        'NAME': 'ubicatech.db', # Proyecto de manera Local 
        # -------------------------------------------------------------------------------------------           
        
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      
        'PORT': '',                     
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Lima'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-PE'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True



# -------------------------------------------------------------------------------------------

# MEDIA_ROOT = '/home/mario555/ubicatech/ubicatech/carga' # Proyecto en Producción

MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'carga') # Proyecto de manera Local

# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------

# MEDIA_URL = 'http://mario555.pythonanywhere.com/media/' # Proyecto en Producción

MEDIA_URL = 'http://127.0.0.1:8000/media/' # Proyecto de manera Local

# -------------------------------------------------------------------------------------------

STATIC_ROOT = '' # Es lo mismo para local como en Producción

# -------------------------------------------------------------------------------------------

# STATIC_URL = 'http://mario555.pythonanywhere.com/static/' # Proyecto en Producción

STATIC_URL = '/static/' # Proyecto de manera Local

# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------

# STATICFILES_DIRS = '/home/mario555/ubicatech/ubicatech/static' # Proyecto en Producción

STATICFILES_DIRS = (os.path.join(RUTA_PROYECTO,'static'),) # Proyecto de manera Local

# -------------------------------------------------------------------------------------------



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm5%(&+eelsk3*6h$dqae0)6!661e@ff++5xum$t$s282p31%5&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ubicatech.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ubicatech.wsgi.application'

# -------------------------------------------------------------------------------------------

# TEMPLATE_DIRS = ('/home/mario555/ubicatech/ubicatech/plantillas'), # Proyecto en Produccion


TEMPLATE_DIRS = (os.path.join(RUTA_PROYECTO,'plantillas'),) # Proyecto de manera Local

# -------------------------------------------------------------------------------------------


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'autocomplete_light', # Innecesario
    'PIL',
    'ubicatech',
    'empresario',
    'negocio',
    'django_cleanup',
    "geoposition",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Configuraciones para enviar mensajes usando gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'correo.sender.2013@gmail.com'
EMAIL_HOST_PASSWORD = 'correo.sender'
EMAIL_PORT = 587
