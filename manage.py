#!/usr/bin/env python
"""Utilidad de Django para tareas administrativas desde la línea de comandos."""
import os
import sys

def main():
    """Ejecuta tareas administrativas."""
    # Establece la configuración predeterminada del proyecto Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_biblioteca.settings')
    try:
        # Importa la función para ejecutar comandos desde la línea de comandos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Muestra un mensaje de error si Django no está instalado o no se encuentra en PYTHONPATH
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? "
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando de Django desde la línea de comandos
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Llama a la función principal si el archivo se ejecuta como script
    main()
