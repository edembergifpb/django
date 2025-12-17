from django.test import TestCase
from django import forms
from edu.forms import CursoForm
from edu.models import Curso

class CursoFormTest(TestCase):
    def test_curso_form_valid(self):
        form_data = {'nome': 'Engenharia de Software'}
        form = CursoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_curso_form_invalid_empty_nome(self):
        form_data = {'nome': ''}
        form = CursoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_curso_form_no_data(self):
        form = CursoForm()
        self.assertFalse(form.is_valid())

    def test_curso_form_save(self):
        form_data = {'nome': 'Administração'}
        form = CursoForm(data=form_data)
        self.assertTrue(form.is_valid())
        curso = form.save()
        self.assertEqual(curso.nome, 'Administração')
        self.assertTrue(Curso.objects.filter(nome='Administração').exists())