from rest_framework import serializers
from .models import Disciplina, Curso


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']
        read_only_fields = ['id']


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'curso', 'carga_horaria']
        read_only_fields = ['id']
    
    def validate_carga_horaria(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "A carga horária deve ser maior que zero"
            )
        return value
