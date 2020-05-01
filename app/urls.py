from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'),     
    path('base/', views.base, name='base'), 
    path('prueba/', views.prueba, name='prueba'), 
    path('cat/', views.cat, name='cat'), 
    path('badmoms/', views.badmoms, name='badmoms'), 
    path('ranking/', views.ranking, name='ranking'),
    path('movielist/', views.movie_list, name='movie_list'),    
    path('register/', views.register, name='register'), 
    path('registry/', views.form_register, name='form_register'), 
    path('login/', views.form_login, name='form_login'), 
    path('authenticate/', views.authenticat, name='authenticat'), 
    path('logout/', views.view_logout, name='view_logout'), 
    path('genres/', views.view_genres, name='view_genres'), 
    path('genres/<int:id>/', views.view_genre, name='view_genre'), 
    path('movies/', views.view_movies, name='view_movies'), 
    path('movies/<int:id>/', views.view_movie, name='view_movie'), 


]