# biblioteca/admin.py

from django.contrib import admin
from .models import Autor, Categoria, Libro, Prestamo, Publicacion, Mensaje, Perfil

# Registro de modelos en el panel de administración
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Publicacion)
admin.site.register(Mensaje)
admin.site.register(Perfil)
