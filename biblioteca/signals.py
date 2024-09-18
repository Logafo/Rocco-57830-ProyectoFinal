# biblioteca/signals.py

from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil, Publicacion
import os

# Crear automáticamente un perfil cuando se crea un nuevo usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

# Guardar el perfil del usuario cada vez que se guarda el usuario
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

@receiver(pre_save, sender=Perfil)
def eliminar_imagen_antigua(sender, instance, **kwargs):
    if not instance.pk:
        return False  # No existe una instancia previa

    try:
        perfil_previo = Perfil.objects.get(pk=instance.pk)
    except Perfil.DoesNotExist:
        return False

    imagen_previa = perfil_previo.imagen
    imagen_nueva = instance.imagen

    if imagen_previa and imagen_previa != imagen_nueva:
        if os.path.isfile(imagen_previa.path):
            os.remove(imagen_previa.path)

@receiver(post_delete, sender=Perfil)
def eliminar_imagen_al_eliminar_perfil(sender, instance, **kwargs):
    imagen = instance.imagen
    if imagen and os.path.isfile(imagen.path):
        os.remove(imagen.path)

@receiver(post_delete, sender=Publicacion)
def eliminar_imagen_publicacion(sender, instance, **kwargs):

    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        # Solo crea un perfil si el usuario ha sido creado
        Perfil.objects.create(user=instance)
    else:
        # Actualiza el perfil existente si el usuario ha sido actualizado
        instance.perfil.save()