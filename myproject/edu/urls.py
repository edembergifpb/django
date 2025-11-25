from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/', views.list_courses, name='list_courses'), 
    path('course/edit/<int:id>', views.edit_course, name='edit_course'),
    # Student CRUD
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<str:pk>/edit/', views.student_update, name='student_update'),
    path('students/<str:pk>/delete/', views.student_delete, name='student_delete'),
    # Auth
    path('signup/', views.signup_view, name='signup'), #Registrar usuário
    path('signin/', views.signin_view, name='signin'), #Login do usuário
    path('logout/', views.logout_view, name='logout'), #Logout do usuário
]