from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from biblioteca import views as biblioteca_views  # Importar las vistas de biblioteca

urlpatterns = [
    # Rutas del admin
    path('admin/', admin.site.urls),
    
    # Incluir las URLs de la app 'biblioteca'
    path('', include('biblioteca.urls')),
    
    # Incluir las URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # URL personalizada para cerrar sesión en el admin
    path('admin/logout/', biblioteca_views.custom_admin_logout, name='admin_logout'),
]

# Servir archivos estáticos y de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
