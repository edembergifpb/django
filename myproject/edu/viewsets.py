from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Disciplina, Curso
from .serializers import DisciplinaSerializer, CursoSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    """Endpoint de login que retorna os dados do usuário autenticado"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Username and password required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(request, username=username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    login(request, user)
    
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_diretor': user.groups.filter(name='diretores').exists()
    }, status=status.HTTP_200_OK)


class IsDiretor(permissions.BasePermission):
    """Permissão customizada: apenas usuários do grupo 'diretores' podem criar cursos"""
    
    def has_permission(self, request, view):
        # Leitura disponível para qualquer um
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Criação apenas para membros do grupo 'diretores'
        if request.method == 'POST':
            if request.user and request.user.is_authenticated:
                return request.user.groups.filter(name='diretores').exists()
            return False
        
        # Outras ações (PUT, DELETE) são proibidas
        return False


class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsDiretor]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.AllowAny]
