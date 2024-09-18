# biblioteca\models.py

# Importaciones necesarias.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from django.core.validators import RegexValidator
import os

# Genera un código único.
def get_unique_code():
    return f"code-{random.randint(100000, 999999)}"

# Genera un código incremental basado en el último ID.
def generate_incremental_code(prefix, model_class):
    last_instance = model_class.objects.order_by('id').last()
    if last_instance:
        last_id = int(last_instance.code.split('-')[-1])
        new_id = last_id + 1
    else:
        new_id = 1
    return f"{prefix}{new_id:06d}"

# Modelo de mensajes entre usuarios.
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.asunto} - {self.remitente}'

# Modelo de perfil de usuario.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    # Elimina la imagen del perfil si es necesario.
    def delete(self, *args, **kwargs):
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Perfil, self).delete(*args, **kwargs)

    # Guarda el perfil y actualiza la imagen.
    def save(self, *args, **kwargs):
        try:
            this = Perfil.objects.get(id=self.id)
            if this.imagen and self.imagen and this.imagen != self.imagen:
                if os.path.isfile(this.imagen.path):
                    os.remove(this.imagen.path)
        except Perfil.DoesNotExist:
            pass
        super(Perfil, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

# Crea o actualiza el perfil al crear o modificar un usuario.
@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        instance.perfil.save()

# Modelo para publicaciones.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    code = models.CharField(max_length=20, unique=True, editable=False)

    # Genera código al guardar.
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code('PUB-', Publicacion)
        super(Publicacion, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

# Modelo para autores.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre

# Modelo para categorías.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    code = models.CharField(max_length=20, unique=True, editable=False)

    # Genera código al guardar.
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code('CAT-', Categoria)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

# Modelo para libros.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_publicacion = models.DateField()
    code = models.CharField(max_length=20, unique=True, editable=False)

    # Genera código al guardar.
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code('LIB-', Libro)
        super(Libro, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

# Modelo para préstamos de libros.
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        fecha_prestamo_formateada = self.fecha_prestamo.strftime('%-d de %B de %Y')
        fecha_devolucion_formateada = self.fecha_devolucion.strftime('%-d de %B de %Y') if self.fecha_devolucion else 'Pendiente'
        return f"{self.libro.titulo} - prestado a {self.nombre} ({self.cedula}) desde el {fecha_prestamo_formateada} hasta el {fecha_devolucion_formateada}"
