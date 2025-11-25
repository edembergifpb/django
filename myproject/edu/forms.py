from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
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



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'email@exemplo.com', 'class': 'input-text'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'input-text'}))


