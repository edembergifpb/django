
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def soma(request, a, b):
    resultado = a + b
    return HttpResponse(f"A soma de {a} + {b} é {resultado}")

def home(request):
    return render(request, 'polls/home.html')
