from django.shortcuts import render
from django.http import HttpResponse
from app.models import Genre, Movie
from django.contrib.auth.models import User	
from django.contrib.auth import authenticate	
from django.contrib.auth import login
from django.contrib.auth import logout
import math
from django.shortcuts import redirect

def index(request):
    genre_list = Genre.objects.all()
    x = genre_list.count()
    x = math.ceil(x/4)
    contexto = {
        'genre_list' : genre_list,
        'iteraciones' : x
    }
    return render(request, 'app/index.html', contexto)

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

def form_login(request):
    return render(request, 'app/log_in.html')

def form_register(request):
    return render(request, 'app/register.html')
 
def register(request):
    # Obtiene los datos
    username = request.POST['username']
    names = request.POST['names']
    email = request.POST['email']
    password = request.POST['password']
 
    # Crea el objeto usuario
    usuario = User(username=username, first_name=names, email=email)
    usuario.set_password(password)
 
    # Guarda el usuario en la base de datos
    usuario.save()
 
    return redirect('app:form_login')

def authenticat(request):
    # Obtiene los datos del formulario de autenticación
    username = request.POST['username']
    password = request.POST['password']
 
    # Obtiene el usuario
    usuario = authenticate(request, username=username, password=password)
 
    # Verifica si el usuario existe en la base de datos 
    if usuario is not None:
        # Inicia la sesión del usuario en el sistema
        login(request, usuario)
        # Redirecciona a una página de éxito
        return redirect('app:index')
    else:
        # Retorna un mensaje de error de login no válido
        return render(request, 'app/login.html') 

def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
 
  # Redirecciona la página de login
  return redirect('app:form_login')

def view_movies(request):
    return HttpResponse()

def view_movie(request, id):
    movie_obj = Movie.objects.get(pk=id)

    contexto = {
        'movie': movie_obj
    }

    return render(request, 'app/movie.html', contexto)



def view_genres(request):
    list_genres = Genre.objects.all()

    contexto = {
        'list_genres': list_genres
    }

    return render(request, 'app/genres.html', contexto)

def view_genre(request, id):
    genre_obj = Genre.objects.get(pk=id)

    contexto = {
        'genre': genre_obj
    }

    return render(request, 'app/genre.html', contexto)

