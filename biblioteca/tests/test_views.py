# biblioteca/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from biblioteca.models import Autor
from django.contrib.auth.models import User
from datetime import date

class ListaAutoresViewTest(TestCase):
    def setUp(self):
        Autor.objects.create(nombre='Gabriel García Márquez', fecha_nacimiento='1927-03-06', nacionalidad='Colombiana')
        Autor.objects.create(nombre='J.K. Rowling', fecha_nacimiento='1965-07-31', nacionalidad='Británica')
    
    def test_lista_autores_respuesta_correcta(self):
        url = reverse('lista_autores')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biblioteca/lista_autores.html')
        self.assertContains(response, 'Gabriel García Márquez')
        self.assertContains(response, 'J.K. Rowling')

class DetalleAutorViewTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre='Gabriel García Márquez',
            fecha_nacimiento=date(1927, 3, 6),
            nacionalidad='Colombiana'
        )

    def test_detalle_autor_respuesta_correcta(self):
        url = reverse('detalle_autor', args=[self.autor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biblioteca/detalle_autor.html')
        self.assertContains(response, self.autor.nombre)
        self.assertContains(response, self.autor.nacionalidad)
        self.assertContains(response, self.autor.fecha_nacimiento.strftime('%d/%m/%Y'))

class CrearAutorViewTest(TestCase):
    def setUp(self):
        self.url = reverse('crear_autor')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
       
    def test_crear_autor_autenticado_pagina_correcta(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biblioteca/crear_autor.html')
    
    def test_crear_autor_post_valido_crea_autor(self):
        datos = {
            'nombre': 'Isaac Asimov',
            'fecha_nacimiento': '02/01/1920',
            'nacionalidad': 'Estadounidense'
        }
        response = self.client.post(self.url, data=datos)
        self.assertEqual(Autor.objects.count(), 1)
        autor = Autor.objects.first()
        self.assertEqual(autor.nombre, 'Isaac Asimov')
        self.assertEqual(autor.fecha_nacimiento, date(1920, 1, 2))
        self.assertEqual(autor.nacionalidad, 'Estadounidense')
        self.assertRedirects(response, reverse('lista_autores'))
