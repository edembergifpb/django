from django import forms
from .models import Curso, Student


# forms.py


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matricula', 'nome', 'date_of_birth', 'email', 'curso']
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Matrícula', 'class': 'input-text'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'input-text'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@exemplo.com', 'class': 'input-text'}),
            'curso': forms.Select(attrs={'class': 'input-text'}),
        }


