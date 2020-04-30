from django.shortcuts import render
from django.http import HttpResponse
from app.models import Genre, Movie
import math

def index(request):
    genre_list = Genre.objects.all()

    x = genre_list.count()
    x = math.ceil(x/4)
    contexto = {
        'genre_list' : genre_list,
        'iteraciones' : x
    }


    return render(request, 'app/index.html', contexto)

def log_in(request):
    return render(request, 'app/log_in.html')

def register(request):
    return render(request, 'app/register.html')

def base(request):    
    return render(request, 'app/base.html')

def prueba(request):
    return render(request, 'app/prueba.html')

def cat(request):
    return render(request, 'app/base.html')

def badmoms(request):
    return render(request, 'app/badmoms.html')

def ranking(request):
    return render(request, 'app/ranking.html')

def movie_list(request):
    return render(request, 'app/movie_list.html')