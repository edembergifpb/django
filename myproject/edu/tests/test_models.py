from django.test import TestCase
from edu.models import Curso

class CursoModelTest(TestCase):
    
    def setUp(self):
        self.curso = Curso.objects.create(
            nome="Python Avançado"
        )
    
    def test_curso_criacao(self):
        self.assertEqual(self.curso.nome, "Python Avançado")
        self.assertTrue(isinstance(self.curso, Curso))
    
    def test_curso_str(self):
        self.assertEqual(str(self.curso), self.curso.nome)
    
    def test_campo_nome_max_length(self):
        self.assertEqual(self.curso._meta.get_field('nome').max_length, 100)