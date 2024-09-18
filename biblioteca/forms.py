# biblioteca/forms.py

from django import forms
from .models import Autor, Categoria, Libro, Prestamo, Publicacion, Perfil, Mensaje
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput
from datetime import date

# Formulario de creación de usuarios personalizados
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electrónico')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Formulario de perfil
class PerfilForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='Nombre de usuario')
    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(max_length=30, required=False, label='Nombre')
    last_name = forms.CharField(max_length=150, required=False, label='Apellido')

    class Meta:
        model = Perfil
        fields = ['imagen']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PerfilForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

        self.fields['imagen'].widget = ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'clearable': False})
        self.fields['imagen'].help_text = ''  

# Formulario de mensajes
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['asunto', 'cuerpo', 'destinatario']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MensajeForm, self).__init__(*args, **kwargs)
        
        # Ocultar destinatario si está respondiendo
        if 'initial' in kwargs and 'destinatario' in kwargs['initial']:
            self.fields['destinatario'].widget = forms.HiddenInput()

    def clean_destinatario(self):
        destinatario = self.cleaned_data.get('destinatario')
        if not destinatario:
            raise forms.ValidationError("Debe seleccionar un destinatario.")
        if destinatario == self.user:
            raise forms.ValidationError("No puedes enviarte mensajes a ti mismo.")
        return destinatario

# Formulario de publicaciones
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'
        exclude = ['autor', 'fecha']

# Formulario de autores
class AutorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento (formato "28/10/1976"):',
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': '28/10/1976'}),
        input_formats=['%d/%m/%Y'],
    )

    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha > date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede estar en el futuro.")
        return fecha

# Formulario de categorías
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        error_messages = {
            'nombre': {'required': 'Este campo es obligatorio.'},
        }

# Formulario de libros
class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label='Fecha de Publicación',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una fecha válida.'
        }
    )

    class Meta:
        model = Libro
        fields = '__all__'

# Formulario de préstamos con validación de fechas
class PrestamoForm(forms.ModelForm):
    cedula = forms.CharField(
        max_length=8,
        label='Cédula del Prestado',
        validators=[RegexValidator(regex=r'^\d{8}$', message='La cédula debe contener exactamente 8 dígitos.')],
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'La cédula debe contener exactamente 8 dígitos sin puntos ni guiones.'
        }
    )
    nombre = forms.CharField(
        max_length=100,
        label='Nombre del Prestado',
        error_messages={
            'required': 'Este campo es obligatorio.'
        }
    )
    fecha_prestamo = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label='Fecha de Préstamo',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una fecha válida.'
        }
    )
    fecha_devolucion = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label='Fecha de Devolución',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una fecha válida.'
        },
        required=False
    )

    class Meta:
        model = Prestamo
        fields = ['cedula', 'nombre', 'fecha_prestamo', 'fecha_devolucion', 'libro']

    def clean(self):
        cleaned_data = super().clean()
        fecha_prestamo = cleaned_data.get("fecha_prestamo")
        fecha_devolucion = cleaned_data.get("fecha_devolucion")

        # Validar que la fecha de devolución no sea anterior a la fecha de préstamo
        if fecha_devolucion and fecha_prestamo and fecha_devolucion < fecha_prestamo:
            self.add_error('fecha_devolucion', "La fecha de devolución no puede ser antes de la fecha de prestado.")
        return cleaned_data

# Formularios de búsqueda
class BuscarLibroForm(forms.Form):
    criterio = forms.CharField(label='Buscar por título', max_length=200, required=False)

class BuscarAutorForm(forms.Form):
    criterio = forms.CharField(label='Buscar por nombre', max_length=100, required=False)

class BuscarCategoriaForm(forms.Form):
    criterio = forms.CharField(label='Buscar por nombre', max_length=100, required=False)

class BuscarPrestamoForm(forms.Form):
    criterio = forms.CharField(label='Buscar por cédula o nombre', max_length=100, required=False)
