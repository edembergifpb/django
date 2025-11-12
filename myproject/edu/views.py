from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import CursoForm, StudentForm

# Create your views here.
def home(request):
    return render(request, "edu/home.html")


def course_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_courses')
    else:
        form = CursoForm()
    return render(request, 'edu/form.html', {'form': form})

def list_courses(request):
    from .models import Curso
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    cursos_list = Curso.objects.all().order_by('nome')
    page = request.GET.get('page', 1)
    paginator = Paginator(cursos_list, 5)  # 5 cursos por página
    try:
        cursos = paginator.page(page)
    except PageNotAnInteger:
        cursos = paginator.page(1)
    except EmptyPage:
        cursos = paginator.page(paginator.num_pages)

    return render(request, 'edu/course_list.html', {'cursos': cursos})

def edit_course(request, id):
    from .models import Curso
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('edu:list_courses')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'edu/form.html', {'form': form})


def student_list(request):
    from .models import Student
    students = Student.objects.select_related('curso').all()
    return render(request, 'edu/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:student_list')
    else:
        form = StudentForm()
    return render(request, 'edu/student_form.html', {'form': form})


def student_update(request, pk):
    from .models import Student
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('edu:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edu/student_form.html', {'form': form})


def student_delete(request, pk):
    from .models import Student
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('edu:student_list')
    return render(request, 'edu/student_confirm_delete.html', {'student': student})
