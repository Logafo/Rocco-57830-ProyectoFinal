# Proyecto Final 

## <img src="https://i.imgur.com/XTt4zIr.png" width="22"> LibroManía - Gestión de Biblioteca 

### Alumno: Christian Rocco  
### Comisión: 57830  
### Proyecto Final

Aplicación web desarrollada con Django que permite gestionar una biblioteca personal o comunitaria. La aplicación facilita la administración de autores, libros, categorías, préstamos y publicaciones de blog relacionadas con la lectura. Además, incluye funcionalidades de autenticación para proteger ciertas acciones y una interfaz amigable para usuarios y administradores.

Actualmente, mi_biblioteca está desplegado en Railway, una plataforma de despliegue que ofrece infraestructura escalable y confiable. Gracias a Railway, la aplicación se beneficia de un despliegue continuo y simplificado, permitiendo actualizaciones rápidas y eficientes sin interrupciones. Railway gestiona automáticamente las configuraciones de entorno y las dependencias, asegurando que mi_biblioteca funcione de manera óptima tanto en entornos de desarrollo como en producción.

### **Acceder a la Aplicación**

Accede a la aplicación a través de [rocco-57830-proyectofinal-production.up.railway.app](rocco-57830-proyectofinal-production.up.railway.app).

## 🛠️ **Características**

- **Gestión de Autores:** Crear, editar y eliminar autores, con información detallada como nombre, fecha de nacimiento y nacionalidad.

- **Gestión de Libros:** Añadir, editar y eliminar libros, categorizándolos por género y asociándolos a autores y editoriales.

- **Categorías:** Organizar los libros en diferentes categorías para facilitar la búsqueda y clasificación.

- **Préstamos:** Registrar y gestionar los préstamos de libros a usuarios.

- **Reservas de Libros:** Permitir a los usuarios reservar libros que están actualmente prestados.

- **Historial de Préstamos:** Mantener un registro histórico de todos los préstamos realizados por los usuarios.

- **Blog de Lectura:** Publicar artículos relacionados con libros, autores, reseñas y eventos literarios.

- **Autenticación de Usuarios y Roles:** Permitir el acceso protegido para acciones sensibles como crear, editar o eliminar registros, y gestionar diferentes roles de usuarios (por ejemplo, administradores, staff, usuarios estándar) con permisos específicos.

- **Tests Automatizados:** Suite de tests para asegurar el correcto funcionamiento de formularios, vistas y otras funcionalidades críticas de la aplicación.

- **Gestión de Usuarios y Permisos:** Administrar usuarios, asignar roles y gestionar permisos para asegurar que cada usuario tenga acceso solo a las funcionalidades que le corresponden.

- **Meta Tags:** El programa incluye meta tags para optimizar la descripción del sitio web:

## 🚀 **Tecnologías Utilizadas**

- **Backend:** Django
- **Base de Datos:** SQLite (desarrollo local) y PostgreSQL (producción en Railway)
- **Frontend:** HTML, CSS, Bootstrap
- **Despliegue:** Railway
- **Otros:** dj_database_url, WhiteNoise


### 📦 **Instalación local**

### 1. **Clonar el Repositorio**

Clona el repositorio desde GitHub y navega al directorio del proyecto.

```bash
git clone https://github.com/Logafo/Rocco-57830-ProyectoFinal
```

```bash
cd Rocco-57830-ProyectoFinal
```

### 2. **Crear un Entorno Virtual**

Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv env
```

Activa el entorno virtual:

- **En Windows:**

  ```bash
  env\Scripts\activate
  ```

- **En Unix o MacOS:**

  ```bash
  source env/bin/activate
  ```

### 3. **Instalar las Dependencias**

Instala todas las dependencias necesarias utilizando el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. **Configurar las Variables de Entorno (.env)**

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

**Pasos para Configurar el Archivo `.env`:**

1. **Crear el Archivo `.env`:**

   En la raíz del proyecto (`Rocco-57830-ProyectoFinal`), crea un archivo llamado `.env`.

  - **En Windows:**

```bash
notepad .env
```
   - **Unix/MacOS:**

```bash
nano .env
```

2. **Añadir el Contenido al Archivo `.env`:**

   Copia y pega el siguiente contenido en el archivo `.env`:

    ```env
    DJANGO_SECRET_KEY=clave_super_secreta_django
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    ```

### 5. **Ejecutar `collectstatic`**

Recopila los archivos estáticos en el directorio especificado.

```bash
python manage.py collectstatic
```

### 6. **Aplicar Migraciones**

Aplica las migraciones para configurar la base de datos local.

```bash
python manage.py migrate
```

### 7. **Crear un Superusuario (Opcional)**

Crea un superusuario para acceder al panel de administración de Django.

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para configurar el superusuario.

## 🏃‍♂️ **Ejecutar la Aplicación en Desarrollo**

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Accede a la aplicación en tu navegador en [`http://localhost:8000/`](http://localhost:8000/).

## 🔬 **Ejecutar los Tests**

El proyecto incluye una suite de tests para asegurar el correcto funcionamiento de formularios y vistas.

### **Cómo Ejecutar los Tests**

1. **Ejecutar los Tests:**

   ```bash
   python manage.py test
   ```

### **Descripción de los Tests**

#### **Tests de Formularios (`test_forms.py`)**

1. **`test_autor_form_valido`**
   - **Descripción:** Verifica que el formulario de Autor se valida correctamente con datos válidos.
   - **Propósito:** Asegurar que los formularios aceptan y procesan datos correctos.

2. **`test_autor_form_sin_nombre`**
   - **Descripción:** Verifica que el formulario de Autor no se valida cuando falta el campo `nombre`.
   - **Propósito:** Garantizar que los campos obligatorios están siendo correctamente validados.

3. **`test_autor_form_fecha_nacimiento_invalida`**
   - **Descripción:** Verifica que el formulario de Autor no se valida cuando la fecha de nacimiento es futura.
   - **Propósito:** Asegurar que los datos ingresados cumplen con las restricciones lógicas (e.g., una fecha de nacimiento no puede estar en el futuro).

#### **Tests de Vistas (`test_views.py`)**

1. **`ListaAutoresViewTest.test_lista_autores_respuesta_correcta`**
   - **Descripción:** Verifica que la vista de listado de autores responde correctamente, utiliza la plantilla adecuada y muestra los autores esperados.
   - **Propósito:** Asegurar que la vista de listado funciona como se espera y muestra la información correcta.

2. **`CrearAutorViewTest.test_crear_autor_post_valido_crea_autor`**
   - **Descripción:** Verifica que un POST válido en la vista de crear autor crea un nuevo autor en la base de datos.
   - **Propósito:** Asegurar que la funcionalidad de creación de autores funciona correctamente y guarda los datos en la base de datos.

## 🎥 **Video de Demostración**
[<img src="https://i.imgur.com/BIDB0J8.png" width="500">](https://youtu.be/bVRdZtEMdp8)

[Mira el video de demostración en YouTube](https://youtu.be/bVRdZtEMdp8)

## 👥 **Contribuciones**

Las contribuciones son bienvenidas. Si desea contribuir al proyecto, por favor, forkee el repositorio y haga una solicitud de extracción con sus cambios.

## 📸 **Capturas de Pantalla**
<img src="https://i.imgur.com/2NaRrtM.png" width="600">

<img src="https://i.imgur.com/s8m1Ot2.png" width="600">

<img src="https://i.imgur.com/nzw9fmc.png" width="600">

<img src="https://i.imgur.com/ZTOeLmm.png" width="600">

<img src="https://i.imgur.com/wM8EEaG.png" width="350">

<img src="https://i.imgur.com/KX2cxNE.png" width="350">

##  **Documentación: git clone y tests**

```bash
C:\temp>git clone https://github.com/Logafo/Rocco-57830-ProyectoFinal
Cloning into 'Rocco-57830-ProyectoFinal'...
remote: Enumerating objects: 70, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 70 (delta 0), reused 6 (delta 0), pack-reused 52 (from 1)
Receiving objects: 100% (70/70), 159.60 KiB | 430.00 KiB/s, done.
Resolving deltas: 100% (6/6), done.

C:\temp>cd Rocco-57830-ProyectoFinal

C:\temp\Rocco-57830-ProyectoFinal>python -m venv env

C:\temp\Rocco-57830-ProyectoFinal>env\Scripts\activate

(env) C:\temp\Rocco-57830-ProyectoFinal>pip install -r requirements.txt
Collecting asgiref==3.8.1 (from -r requirements.txt (line 1))
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting dj-database-url==2.2.0 (from -r requirements.txt (line 2))
  Using cached dj_database_url-2.2.0-py3-none-any.whl.metadata (12 kB)
Collecting Django==5.1.1 (from -r requirements.txt (line 3))
  Using cached Django-5.1.1-py3-none-any.whl.metadata (4.2 kB)
Collecting django-environ==0.11.2 (from -r requirements.txt (line 4))
  Using cached django_environ-0.11.2-py2.py3-none-any.whl.metadata (11 kB)
Collecting gunicorn==23.0.0 (from -r requirements.txt (line 5))
  Using cached gunicorn-23.0.0-py3-none-any.whl.metadata (4.4 kB)
Collecting packaging==24.1 (from -r requirements.txt (line 6))
  Using cached packaging-24.1-py3-none-any.whl.metadata (3.2 kB)
Collecting pillow==10.4.0 (from -r requirements.txt (line 7))
  Using cached pillow-10.4.0-cp312-cp312-win_amd64.whl.metadata (9.3 kB)
Collecting psycopg2==2.9.9 (from -r requirements.txt (line 8))
  Using cached psycopg2-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.5 kB)
Collecting python-dotenv==1.0.1 (from -r requirements.txt (line 9))
  Using cached python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Collecting sqlparse==0.5.1 (from -r requirements.txt (line 10))
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Collecting typing_extensions==4.12.2 (from -r requirements.txt (line 11))
  Using cached typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting tzdata==2024.1 (from -r requirements.txt (line 12))
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting whitenoise==6.7.0 (from -r requirements.txt (line 13))
  Using cached whitenoise-6.7.0-py3-none-any.whl.metadata (3.7 kB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached dj_database_url-2.2.0-py3-none-any.whl (7.8 kB)
Using cached Django-5.1.1-py3-none-any.whl (8.2 MB)
Using cached django_environ-0.11.2-py2.py3-none-any.whl (19 kB)
Using cached gunicorn-23.0.0-py3-none-any.whl (85 kB)
Using cached packaging-24.1-py3-none-any.whl (53 kB)
Using cached pillow-10.4.0-cp312-cp312-win_amd64.whl (2.6 MB)
Using cached psycopg2-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)
Using cached python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Using cached whitenoise-6.7.0-py3-none-any.whl (19 kB)
Installing collected packages: whitenoise, tzdata, typing_extensions, sqlparse, python-dotenv, psycopg2, pillow, packaging, django-environ, asgiref, gunicorn, Django, dj-database-url
Successfully installed Django-5.1.1 asgiref-3.8.1 dj-database-url-2.2.0 django-environ-0.11.2 gunicorn-23.0.0 packaging-24.1 pillow-10.4.0 psycopg2-2.9.9 python-dotenv-1.0.1 sqlparse-0.5.1 typing_extensions-4.12.2 tzdata-2024.1 whitenoise-6.7.0

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(env) C:\temp\Rocco-57830-ProyectoFinal>notepad .env

(env) C:\temp\Rocco-57830-ProyectoFinal>python manage.py collectstatic

131 static files copied to 'C:\temp\Rocco-57830-ProyectoFinal\staticfiles'.

(env) C:\temp\Rocco-57830-ProyectoFinal>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, biblioteca, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying biblioteca.0001_initial... OK
  Applying biblioteca.0002_create_superuser...Variables de entorno para el superusuario no están definidas.
 OK
  Applying sessions.0001_initial... OK

(env) C:\temp\Rocco-57830-ProyectoFinal>python manage.py createsuperuser
Nombre de usuario (leave blank to use 'chris'): admin
Dirección de correo electrónico:
Password:
Password (again):
Superuser created successfully.

(env) C:\temp\Rocco-57830-ProyectoFinal>python manage.py test
Found 7 test(s).
Creating test database for alias 'default'...
Variables de entorno para el superusuario no están definidas.
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 4.174s

OK
Destroying test database for alias 'default'...

(env) C:\temp\Rocco-57830-ProyectoFinal>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 22, 2024 - 00:39:21
Django version 5.1.1, using settings 'mi_biblioteca.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Estructura del Repositorio

La siguiente es la estructura completa del repositorio, mostrando todos los archivos y carpetas principales:

```
.
│   .gitignore                       # Archivo que especifica los archivos y carpetas que Git debe ignorar
│   manage.py                        # Utilidad de línea de comandos para administrar el proyecto Django
│   procfile                         # Archivo de configuración para indicar a Railway cómo ejecutar la aplicación
│   README.md                        # Archivo de documentación principal del proyecto
│   requirements.txt                  # Lista de dependencias de Python que necesita el proyecto
│
├───biblioteca
│   │   admin.py                      # Configuraciones para el panel de administración de Django
│   │   apps.py                       # Configuración de la aplicación 'biblioteca'
│   │   context_processors.py         # Procesadores de contexto personalizados para las plantillas
│   │   forms.py                      # Definición de formularios personalizados
│   │   models.py                     # Definición de los modelos de datos de la aplicación
│   │   signals.py                    # Señales para manejar eventos específicos (ej. crear superusuario)
│   │   urls.py                       # Rutas específicas de la aplicación 'biblioteca'
│   │   views.py                      # Vistas que manejan la lógica de las solicitudes HTTP
│   │   __init__.py                   # Indica que este directorio es un paquete de Python
│   │
│   ├───migrations
│   │       0001_initial.py           # Migración inicial que crea las tablas de la base de datos
│   │       0002_create_superuser.py  # Migración para crear el superusuario por defecto
│   │       __init__.py               # Indica que este directorio es un paquete de Python
│   │
│   ├───templatetags
│   │       form_tags.py               # Etiquetas de plantilla personalizadas para formularios
│   │
│   └───tests
│           test_forms.py             # Pruebas automatizadas para los formularios
│           test_views.py             # Pruebas automatizadas para las vistas
│           __init__.py               # Indica que este directorio es un paquete de Python
│
├───mi_biblioteca
│       asgi.py                       # Configuración para servidores compatibles con ASGI
│       settings.py                   # Configuración principal de Django para todos los entornos
│       settings_dev.py               # Configuraciones adicionales específicas para desarrollo local
│       urls.py                       # Rutas URL globales del proyecto
│       wsgi.py                       # Configuración para servidores compatibles con WSGI
│       __init__.py                   # Indica que este directorio es un paquete de Python
│
├───static
│       biblioteca.jpg                # Archivo de imagen estática utilizado en la aplicación
│       favicon.ico                   # Icono de favicon para el sitio web
│       input.png                     # Imagen estática adicional
│       styles.css                    # Archivo CSS para estilos personalizados de la aplicación
│
└───templates
    ├───biblioteca
    │       about.html                 # Página "Acerca de" de la biblioteca
    │       base.html                  # Plantilla base que otras plantillas extienden
    │       crear_autor.html           # Formulario para crear un nuevo autor
    │       crear_categoria.html       # Formulario para crear una nueva categoría
    │       crear_libro.html           # Formulario para crear un nuevo libro
    │       crear_mensaje.html         # Formulario para crear un nuevo mensaje
    │       crear_prestamo.html        # Formulario para registrar un nuevo préstamo
    │       crear_publicacion.html     # Formulario para crear una nueva publicación en el blog
    │       detalle_autor.html          # Detalle de un autor específico
    │       detalle_categoria.html      # Detalle de una categoría específica
    │       detalle_libro.html          # Detalle de un libro específico
    │       detalle_mensaje.html        # Detalle de un mensaje específico
    │       detalle_prestamo.html       # Detalle de un préstamo específico
    │       detalle_publicacion.html    # Detalle de una publicación específica
    │       eliminar_autor.html         # Confirmación para eliminar un autor
    │       eliminar_categoria.html     # Confirmación para eliminar una categoría
    │       eliminar_libro.html         # Confirmación para eliminar un libro
    │       eliminar_mensaje.html       # Confirmación para eliminar un mensaje
    │       eliminar_prestamo.html      # Confirmación para eliminar un préstamo
    │       eliminar_publicacion.html   # Confirmación para eliminar una publicación
    │       inicio.html                 # Página de inicio de la aplicación
    │       lista_autores.html          # Lista de todos los autores
    │       lista_categorias.html       # Lista de todas las categorías
    │       lista_libros.html           # Lista de todos los libros
    │       lista_mensajes.html         # Lista de todos los mensajes
    │       lista_prestamos.html        # Lista de todos los préstamos
    │       lista_publicaciones.html     # Lista de todas las publicaciones en el blog
    │       perfil.html                 # Página de perfil del usuario
    │
    └───registration
            login.html                  # Página de inicio de sesión de usuarios
            signup.html                 # Página de registro de nuevos usuarios
```
