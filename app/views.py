from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo")

def cat(request):
    return render(request, 'app/cat.html')