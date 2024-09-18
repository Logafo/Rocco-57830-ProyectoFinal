# biblioteca/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.db.models import Q
from .models import Autor, Categoria, Libro, Prestamo, Publicacion, Mensaje
from .forms import (
    AutorForm, CategoriaForm, LibroForm, PrestamoForm,
    BuscarLibroForm, BuscarAutorForm, BuscarCategoriaForm, BuscarPrestamoForm,
    PublicacionForm, MensajeForm, PerfilForm, CustomUserCreationForm
)
from django.contrib import messages
from django import forms

def inicio(request):
    return render(request, 'biblioteca/inicio.html')

def about(request):
    return render(request, 'biblioteca/about.html')

# -------------------------------
# Manejo de Mensajes
# -------------------------------

@login_required
def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == 'POST':
        mensaje.delete()
        messages.success(request, "Mensaje eliminado exitosamente.")
        return redirect('lista_mensajes')
    return render(request, 'biblioteca/eliminar_mensaje.html', {'mensaje': mensaje})

@login_required
def crear_mensaje(request):
    reply_to_id = request.GET.get('reply_to')
    destinatario = None
    if reply_to_id:
        mensaje_original = get_object_or_404(Mensaje, pk=reply_to_id)
        destinatario = mensaje_original.remitente

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            if destinatario:
                mensaje.destinatario = destinatario
            mensaje.save()
            messages.success(request, "Mensaje enviado exitosamente.")
            return redirect('lista_mensajes')
    else:
        if destinatario:
            form = MensajeForm(initial={'destinatario': destinatario})
            form.fields['destinatario'].widget = forms.HiddenInput()
        else:
            form = MensajeForm()

    context = {
        'form': form,
        'destinatario': destinatario,
    }
    return render(request, 'biblioteca/crear_mensaje.html', context)

@login_required
def detalle_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.user == mensaje.destinatario and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'biblioteca/detalle_mensaje.html', {'mensaje': mensaje})

@login_required
def lista_mensajes(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'biblioteca/lista_mensajes.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados,
    })

# -------------------------------
# Gestión de Perfiles y Autenticación
# -------------------------------

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            messages.success(request, "Registro exitoso. Has iniciado sesión.")
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES, user=request.user, instance=request.user.perfil)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        
        # Actualizar datos del usuario
        if 'update_profile' in request.POST:
            if perfil_form.is_valid():
                perfil_form.save()
                user = request.user
                user.username = perfil_form.cleaned_data['username']
                user.email = perfil_form.cleaned_data['email']
                user.first_name = perfil_form.cleaned_data['first_name']
                user.last_name = perfil_form.cleaned_data['last_name']
                user.save()
                messages.success(request, "Perfil actualizado exitosamente.")
                return redirect('perfil')
        
        # Cambiar contraseña
        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Mantiene la sesión iniciada
                messages.success(request, "Contraseña cambiada exitosamente.")
                return redirect('perfil')
    else:
        perfil_form = PerfilForm(user=request.user, instance=request.user.perfil)
        password_form = PasswordChangeForm(user=request.user)

    context = {
        'perfil_form': perfil_form,
        'password_form': password_form,
    }
    return render(request, 'biblioteca/perfil.html', context)

@login_required
def eliminar_imagen_perfil(request):
    if request.method == 'POST':
        perfil = request.user.perfil
        if perfil.imagen:
            perfil.imagen.delete(save=True)
            messages.success(request, "La imagen de perfil ha sido eliminada correctamente.")
        else:
            messages.warning(request, "No hay imagen de perfil para eliminar.")
    return redirect('perfil')

def custom_admin_logout(request):
    logout(request)
    return redirect('home')

def logout_page(request):
    return render(request, 'home')

def custom_admin_logout(request):
    logout(request)
    return redirect('inicio')
# -------------------------------
# Manejo de Publicaciones
# -------------------------------

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    mensaje = ""
    if not publicaciones:
        mensaje = "No hay páginas aún."
    return render(request, 'biblioteca/lista_publicaciones.html', {'publicaciones': publicaciones, 'mensaje': mensaje})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'biblioteca/detalle_publicacion.html', {'publicacion': publicacion})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, "Publicación creada exitosamente.")
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'biblioteca/crear_publicacion.html', {'form': form})

@staff_member_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada exitosamente.")
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'biblioteca/crear_publicacion.html', {'form': form})

@staff_member_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        messages.success(request, "Publicación eliminada exitosamente.")
        return redirect('lista_publicaciones')
    return render(request, 'biblioteca/eliminar_publicacion.html', {'publicacion': publicacion})

# -------------------------------
# Gestión de Categorías
# -------------------------------

def lista_categorias(request):
    form = BuscarCategoriaForm(request.GET)
    categorias = Categoria.objects.all()
    if form.is_valid():
        criterio = form.cleaned_data.get('criterio')
        if criterio:
            categorias = categorias.filter(nombre__icontains=criterio)
    return render(request, 'biblioteca/lista_categorias.html', {'categorias': categorias, 'form': form})

def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'biblioteca/detalle_categoria.html', {'categoria': categoria})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'biblioteca/crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'biblioteca/crear_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, "Categoría eliminada exitosamente.")
        return redirect('lista_categorias')
    return render(request, 'biblioteca/eliminar_categoria.html', {'categoria': categoria})

# -------------------------------
# Manejo de Libros
# -------------------------------

def lista_libros(request):
    form = BuscarLibroForm(request.GET)
    libros = Libro.objects.all()
    if form.is_valid():
        criterio = form.cleaned_data.get('criterio')
        if criterio:
            libros = libros.filter(titulo__icontains=criterio)
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros, 'form': form})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'biblioteca/detalle_libro.html', {'libro': libro})

@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "Libro eliminado exitosamente.")
        return redirect('lista_libros')
    return render(request, 'biblioteca/eliminar_libro.html', {'libro': libro})

# -------------------------------
# Manejo de Préstamos
# -------------------------------

@login_required
def lista_prestamos(request):
    form = BuscarPrestamoForm(request.GET)
    prestamos = Prestamo.objects.all()
    if form.is_valid():
        criterio = form.cleaned_data.get('criterio')
        if criterio:
            prestamos = prestamos.filter(
                Q(cedula__icontains=criterio) |
                Q(nombre__icontains=criterio)
            )
    return render(request, 'biblioteca/lista_prestamos.html', {'prestamos': prestamos, 'form': form})

@login_required
def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Préstamo creado exitosamente.")
            return redirect('lista_prestamos')
        else:
            messages.error(request, "Error en la creación del préstamo. Verifique los datos.")
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/crear_prestamo.html', {'form': form})

@login_required
def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'biblioteca/detalle_prestamo.html', {'prestamo': prestamo})

@login_required
def editar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, "Préstamo actualizado exitosamente.")
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'biblioteca/crear_prestamo.html', {'form': form})

@login_required
def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, "Préstamo eliminado exitosamente.")
        return redirect('lista_prestamos')
    return render(request, 'biblioteca/eliminar_prestamo.html', {'prestamo': prestamo})

# -------------------------------
# Manejo de Autores
# -------------------------------

def lista_autores(request):
    form = BuscarAutorForm(request.GET)
    autores = Autor.objects.all()
    if form.is_valid():
        criterio = form.cleaned_data.get('criterio')
        if criterio:
            autores = autores.filter(nombre__icontains=criterio)
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores, 'form': form})

def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    libros = Libro.objects.filter(autor=autor)
    return render(request, 'biblioteca/detalle_autor.html', {'autor': autor, 'libros': libros})

@login_required
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            messages.success(request, f"Autor '{autor.nombre}' creado exitosamente.")
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/crear_autor.html', {'form': form})

@login_required
def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor actualizado exitosamente.")
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/crear_autor.html', {'form': form})

@login_required
def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, "Autor eliminado exitosamente.")
        return redirect('lista_autores')
    return render(request, 'biblioteca/eliminar_autor.html', {'autor': autor})
