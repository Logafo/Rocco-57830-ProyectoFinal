# mi_biblioteca/settings_dev.py

from pathlib import Path

DEBUG = True

# Definición del directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Hosts permitidos para desarrollo local
ALLOWED_HOSTS = [
    'localhost',  
    '127.0.0.1',  
    '.railway.app' 
]

# Configuración de la base de datos para desarrollo local (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de archivos estáticos para desarrollo local


