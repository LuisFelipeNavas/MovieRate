from django.shortcuts import render
from django.http import HttpResponse
from app.models import Genre, User, Comment, Score, Movie
from django.contrib.auth.models import User	
from django.contrib.auth import authenticate	
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Avg

def index(request):
    billboard = Movie.objects.filter(onBillboard=True)       
    genre_list = Genre.objects.all()
    latest_movies = Movie.objects.all().order_by('-id')[:3]
    
    contexto = {
        'genre_list' : genre_list,
        'billboard' : billboard,
        'latest_movies' : latest_movies
    }
    return render(request, 'app/index.html', contexto)

def ranking(request):
    genre_list = Genre.objects.all()
    averages=[]
    movie_list =  Movie.objects.all()
    counter = 1
    for p in movie_list:
	    averages.append({'title': p.title, 'year': p.year, 'duration': p.duration, 'average_score': Score.objects.filter(movie__id=counter).aggregate(average_score=Avg('value')).get("average_score")})	
	    counter += 1

    for i in range(0,len(averages)):
	    if averages[i].get("average_score") == None:
		    averages[i]['average_score']=0
	    else:
    		pass

    averages_list = sorted(averages, key = lambda i: i['average_score'], reverse=True)

    contexto = {
       'averages_list' : averages_list,
       'movie_list' : movie_list,
       'genre_list' : genre_list
    }
    return render(request, 'app/ranking.html', contexto)

def movie_list(request):
    genre_list = Genre.objects.all()
    movies_list = Movie.objects.all()
    movie_a = movies_list.filter(title__startswith='a')
    movie_b = movies_list.filter(title__startswith='b')
    movie_c = movies_list.filter(title__startswith='c')
    movie_d = movies_list.filter(title__startswith='d')
    movie_e = movies_list.filter(title__startswith='e')
    movie_f = movies_list.filter(title__startswith='f')
    movie_g = movies_list.filter(title__startswith='g')
    movie_h = movies_list.filter(title__startswith='h')
    movie_i = movies_list.filter(title__startswith='i')
    movie_j = movies_list.filter(title__startswith='j')
    movie_k = movies_list.filter(title__startswith='k')
    movie_l = movies_list.filter(title__startswith='l')
    movie_m = movies_list.filter(title__startswith='m')
    movie_n = movies_list.filter(title__startswith='n')
    movie_o = movies_list.filter(title__startswith='o')
    movie_p = movies_list.filter(title__startswith='p')
    movie_q = movies_list.filter(title__startswith='q')
    movie_r = movies_list.filter(title__startswith='r')
    movie_s = movies_list.filter(title__startswith='s')
    movie_t = movies_list.filter(title__startswith='t')
    movie_u = movies_list.filter(title__startswith='u')
    movie_v = movies_list.filter(title__startswith='v')
    movie_w = movies_list.filter(title__startswith='w')
    movie_x = movies_list.filter(title__startswith='x')
    movie_y = movies_list.filter(title__startswith='y')
    movie_z = movies_list.filter(title__startswith='z')

    contexto = {
        'movies_list' : movies_list,
        'movie_a' : movie_a,
        'movie_b' : movie_b,
        'movie_c' : movie_c,
        'movie_d' : movie_d,
        'movie_e' : movie_e,
        'movie_f' : movie_f,
        'movie_g' : movie_g,
        'movie_h' : movie_h,
        'movie_i' : movie_i,
        'movie_j' : movie_j,
        'movie_k' : movie_k,
        'movie_l' : movie_l,
        'movie_m' : movie_m,
        'movie_n' : movie_n,
        'movie_o' : movie_o,
        'movie_p' : movie_p,
        'movie_q' : movie_q,
        'movie_r' : movie_r,
        'movie_s' : movie_s,
        'movie_t' : movie_t,
        'movie_u' : movie_u,
        'movie_v' : movie_v,
        'movie_w' : movie_w,
        'movie_x' : movie_x,
        'movie_y' : movie_y,
        'movie_z' : movie_z, 
        'genre_list' : genre_list
    }
    return render(request, 'app/movie_list.html', contexto)

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
        return render(request, 'app/log_in.html') 

def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
 
  # Redirecciona la página de login
  return redirect('app:index')

# def view_movies(request):
#     return HttpResponse()

def view_movie(request, id):
    genre_list = Genre.objects.all()
    movie_obj = Movie.objects.get(pk=id)

    contexto = {
        'movie': movie_obj,
        'genre_list' : genre_list
    }
    return render(request, 'app/movie.html', contexto)

def view_genres(request):
    genre_list = Genre.objects.all()
    list_genres = Genre.objects.all()

    contexto = {
        'list_genres': list_genres,
        'genre_list' : genre_list
    }
    return render(request, 'app/genres.html', contexto)

def view_genre(request, id):
    genre_obj = Genre.objects.get(pk=id)
    genre_list = Genre.objects.all()

    contexto = {
        'genre': genre_obj,
        'genre_list' : genre_list
    }
    return render(request, 'app/genre.html', contexto)