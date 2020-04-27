from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app/index.html')

def cat(request):
    return render(request, 'app/cat.html')

def log_in(request):
    return render(request, 'app/log_in.html')

def register(request):
    return render(request, 'app/register.html')

def base(request):
    return render(request, 'app/base.html')

def prueba(request):
    return render(request, 'app/prueba.html')