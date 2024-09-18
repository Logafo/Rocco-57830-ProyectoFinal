# biblioteca/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Páginas principales
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),

    # Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),  
    path('autores/<int:pk>/', views.detalle_autor, name='detalle_autor'),  
    path('autores/crear/', views.crear_autor, name='crear_autor'),  
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),  
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),  

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),  
    path('categorias/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),  
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),  
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),  
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),  

    # Préstamos
    path('lista_prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('crear_prestamo/', views.crear_prestamo, name='crear_prestamo'),
    path('prestamos/detalle/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('editar_prestamo/<int:prestamo_id>/', views.editar_prestamo, name='editar_prestamo'),
    path('eliminar_prestamo/<int:prestamo_id>/', views.eliminar_prestamo, name='eliminar_prestamo'),

    # Publicaciones
    path('pages/', views.lista_publicaciones, name='lista_publicaciones'),
    path('pages/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('pages/crear/', views.crear_publicacion, name='crear_publicacion'),
    path('pages/editar/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('pages/eliminar/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),

    # Perfil
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/eliminar_imagen/', views.eliminar_imagen_perfil, name='eliminar_imagen_perfil'),
    path('accounts/profile/', views.perfil, name='perfil'),

    # Mensajes
    path('mensajes/', views.lista_mensajes, name='lista_mensajes'),
    path('crear_mensaje/', views.crear_mensaje, name='crear_mensaje'),
    path('mensajes/<int:pk>/', views.detalle_mensaje, name='detalle_mensaje'),
    path('mensajes/eliminar/<int:pk>/', views.eliminar_mensaje, name='eliminar_mensaje'),

    # Autenticación
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
