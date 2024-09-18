# biblioteca/context_processors.py

from .models import Mensaje

# Procesador de contexto para obtener el número de mensajes no leídos
def mensajes_sin_leer(request):
    if request.user.is_authenticated:
        # Si el usuario está autenticado, se cuentan los mensajes no leídos
        mensajes_no_leidos = Mensaje.objects.filter(destinatario=request.user, leido=False).count()
    else:
        # Si no está autenticado, el contador de mensajes no leídos es 0
        mensajes_no_leidos = 0
    return {'mensajes_no_leidos': mensajes_no_leidos}
