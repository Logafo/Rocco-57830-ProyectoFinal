# biblioteca/tests/test_forms.py

from django.test import TestCase
from biblioteca.forms import AutorForm

class AutorFormTest(TestCase):
    def test_autor_form_valido(self):
        datos = {
            'nombre': 'Gabriel García Márquez',
            'fecha_nacimiento': '06/03/1927',
            'nacionalidad': 'Colombiana'
        }
        form = AutorForm(data=datos)
        self.assertTrue(form.is_valid())

    def test_autor_form_sin_nombre(self):
        datos = {
            'fecha_nacimiento': '1927-03-06',
            'nacionalidad': 'Colombiana'
        }
        form = AutorForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)

    def test_autor_form_fecha_nacimiento_invalida(self):
        datos = {
            'nombre': 'Gabriel García Márquez',
            'fecha_nacimiento': '3000-01-01',
            'nacionalidad': 'Colombiana'
        }
        form = AutorForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('fecha_nacimiento', form.errors)
