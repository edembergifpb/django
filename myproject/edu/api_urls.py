from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import DisciplinaViewSet, CursoViewSet, login_view

router = SimpleRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)

app_name = 'api'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', include(router.urls)),
]
