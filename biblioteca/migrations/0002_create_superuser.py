# biblioteca\migrations\0002_create_superuser.py

# Importaciones necesarias.
from django.db import migrations
from django.contrib.auth import get_user_model
import os

# Función para crear un superusuario utilizando variables de entorno.
def create_superuser(apps, schema_editor):
    User = get_user_model()  # Obtiene el modelo de usuario.
    username = os.environ.get('SUPERUSER_USERNAME')
    email = os.environ.get('SUPERUSER_EMAIL')
    password = os.environ.get('SUPERUSER_PASSWORD')
    
    # Verifica si las variables de entorno están definidas.
    if username and password:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superusuario '{username}' creado exitosamente.")
        else:
            print(f"Superusuario '{username}' ya existe.")
    else:
        print("Variables de entorno para el superusuario no están definidas.")

# Función para eliminar un superusuario.
def delete_superuser(apps, schema_editor):
    User = get_user_model()
    username = os.environ.get('SUPERUSER_USERNAME')
    if username:
        try:
            user = User.objects.get(username=username)
            user.delete()
            print(f"Superusuario '{username}' eliminado exitosamente.")
        except User.DoesNotExist:
            print(f"Superusuario '{username}' no existe.")

# Definición de la clase de migración.
class Migration(migrations.Migration):

    # Dependencia de la migración inicial.
    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    # Operaciones de la migración.
    operations = [
        # Ejecuta las funciones de creación y eliminación del superusuario.
        migrations.RunPython(create_superuser, delete_superuser),
    ]
