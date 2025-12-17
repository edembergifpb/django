from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from edu.models import Curso

class ListCoursesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('edu:list_courses')
        # Create test courses
        for i in range(7):
            Curso.objects.create(nome=f'Curso {i}')

    def test_list_courses_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_list_courses_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'edu/course_list.html')

    def test_list_courses_pagination(self):
        response = self.client.get(self.url)
        self.assertTrue('cursos' in response.context)
        self.assertEqual(len(response.context['cursos']), 5)

    def test_list_courses_second_page(self):
        response = self.client.get(self.url + '?page=2')
        self.assertTrue('cursos' in response.context)
        self.assertEqual(len(response.context['cursos']), 2)

    def test_list_courses_invalid_page(self):
        response = self.client.get(self.url + '?page=invalid')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cursos']), 5)

    def test_list_courses_ordered_by_name(self):
        response = self.client.get(self.url)
        cursos = response.context['cursos']
        self.assertEqual(cursos[0].nome, 'Curso 0')