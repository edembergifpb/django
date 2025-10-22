from django.contrib import admin
from .models import Student, Curso, Disciplina, Matricula


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('matricula', 'nome', 'email',"curso")
	search_fields = ('matricula', 'nome', 'email')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ('nome',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso', 'carga_horaria')
    search_fields = ('nome', 'curso__nome')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'disciplina', 'semestre')
    search_fields = ('student__nome', 'disciplina__nome', 'semestre')

