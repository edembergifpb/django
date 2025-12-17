from django.test import TestCase
from edu.models import Disciplina, Curso
from edu.serializers import DisciplinaSerializer

class DisciplinaSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(nome='Engenharia')
        self.disciplina_data = {
            'nome': 'Programação',
            'curso': self.curso.id,
            'carga_horaria': 60
        }

    def test_serializer_with_valid_data(self):
        serializer = DisciplinaSerializer(data=self.disciplina_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_carga_horaria_zero(self):
        self.disciplina_data['carga_horaria'] = 0
        serializer = DisciplinaSerializer(data=self.disciplina_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('carga_horaria', serializer.errors)

    def test_serializer_with_invalid_carga_horaria_negative(self):
        self.disciplina_data['carga_horaria'] = -10
        serializer = DisciplinaSerializer(data=self.disciplina_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_creates_disciplina(self):
        serializer = DisciplinaSerializer(data=self.disciplina_data)
        self.assertTrue(serializer.is_valid())
        disciplina = serializer.save()
        self.assertEqual(disciplina.nome, 'Programação')
        self.assertEqual(disciplina.carga_horaria, 60)

    def test_serializer_id_is_read_only(self):
        self.disciplina_data['id'] = 999
        serializer = DisciplinaSerializer(data=self.disciplina_data)
        self.assertTrue(serializer.is_valid())
        disciplina = serializer.save()
        self.assertNotEqual(disciplina.id, 999)