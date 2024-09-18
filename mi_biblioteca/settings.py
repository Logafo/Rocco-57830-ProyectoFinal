# mi_biblioteca/settings.py

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

DEBUG = False 

# Definición del directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
load_dotenv(BASE_DIR / '.env')

# Redirección después de cerrar sesión
LOGOUT_REDIRECT_URL = 'inicio'

# Seguridad
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure--!@$m0iwk2s_co9kqg&c)xihc54f)p(dhshhu!sbyt!ogq028*')

DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() in ['true', '1', 't']

# Hosts permitidos
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'biblioteca.apps.BibliotecaConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

if not DEBUG:
    # Middleware específico de producción
    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

MIDDLEWARE += [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL raíz
ROOT_URLCONF = 'mi_biblioteca.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta a la carpeta de plantillas
        'APP_DIRS': True,  # Activa la búsqueda automática de plantillas en las aplicaciones
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'biblioteca.context_processors.mensajes_sin_leer',
            ],
        },
    },
]

# Aplicación WSGI
WSGI_APPLICATION = 'mi_biblioteca.wsgi.application'

# Importar configuraciones adicionales para desarrollo
try:
    from .settings_dev import *
except ModuleNotFoundError:
    pass

# Configuración de la base de datos
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

APPEND_SLASH = True

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización
LANGUAGE_CODE = 'es'  # Idioma español
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Formatos de entrada de fecha
DATE_INPUT_FORMATS = ['%d/%m/%Y']  # dd/mm/aaaa

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio para los archivos recolectados en producción

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # Directorio donde están los archivos estáticos durante el desarrollo
]

# Configuración de archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

if not DEBUG:
    # Usar WhiteNoise para gestionar archivos estáticos en producción
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    # Configuración para desarrollo local
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Orígenes confiables para CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://rocco-57830-proyectofinal-production.up.railway.app',
]


