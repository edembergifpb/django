from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_not_whitespace(value):
	"""Validador que rejeita valores vazios ou compostos apenas por espaços."""
	if value is None or not str(value).strip():
		raise ValidationError(_("This field cannot be blank or contain only whitespace."), code="blank")


class Student(models.Model):
	"""Representa um estudante.

	Campos:
	- matricula: string usada como chave primária
	- nome: até 150 chars, obrigatório e não pode ser apenas espaços
	- date_of_birth: data de nascimento, obrigatório
	- email: obrigatório e único
	"""

	matricula = models.CharField(max_length=30, primary_key=True)
	nome = models.CharField(max_length=150, null=False, blank=False, validators=[validate_not_whitespace])
	date_of_birth = models.DateField(null=False, blank=False)
	email = models.EmailField(unique=True, null=False, blank=False)
	curso = models.ForeignKey('Curso', on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f"{self.matricula} - {self.nome}"


class Curso(models.Model):
	"""Representa um curso simples com nome obrigatório."""

	nome = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False,unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    carga_horaria = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='matriculas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='matriculas')
    semestre = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'disciplina', 'semestre'], name='unique_student_disciplina_semestre')
        ]

    def __str__(self):
        return f"{self.student.matricula} - {self.disciplina.nome} - {self.semestre}"
