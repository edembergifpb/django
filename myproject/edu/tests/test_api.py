from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from edu.models import Disciplina,Curso

class DisciplinaAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.curso = Curso.objects.create(nome='Matematica')     

    def test_list_items(self):
        response = self.client.get('/edu/api/disciplinas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_item(self):      
        self.disciplina = Disciplina.objects.create(nome='Calculo I',
                                                    carga_horaria=100,
                                                    curso=self.curso)  
        response = self.client.get(f'/edu/api/disciplinas/{self.disciplina.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item(self):
        data = {
            "nome": "Calculo I",
            "carga_horaria": 100,
            "curso":self.curso.id
        }
        response = self.client.post('/edu/api/disciplinas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,response.data)