from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import HttpResponseNotAllowed
from .forms import CursoForm, StudentForm, SignUpForm, SignInForm

# Create your views here.
def home(request):
    return render(request, "edu/home.html")


from django.http import HttpResponseNotAllowed


@permission_required('edu.add_curso')
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

@permission_required('edu.change_curso')
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


@permission_required('edu.delete_curso')
def delete_course(request, id):
    from .models import Curso
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('edu:list_courses')
    return render(request, 'edu/course_confirm_delete.html', {'curso': curso})


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


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edu:home')
    else:
        form = SignUpForm()
    return render(request, 'edu/sign_up.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('edu:home')
    else:
        form = SignInForm()
    return render(request, 'edu/sign_in.html', {'form': form})


def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    logout(request)
    return redirect('edu:signin')
