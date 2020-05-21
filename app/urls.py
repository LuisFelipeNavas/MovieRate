from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'),       
    path('ranking/', views.ranking, name='ranking'),
    path('movieslist/', views.movies_list, name='movies_list'),    

    #path('movielist/<int:id>/', views.movie_list, name='movie_list'),    

    path('register/', views.register, name='register'), 
    path('registry/', views.form_register, name='form_register'), 
    path('login/', views.form_login, name='form_login'), 
    path('authenticate/', views.authenticat, name='authenticat'), 
    path('logout/', views.view_logout, name='view_logout'), 
    path('genres/', views.view_genres, name='view_genres'), 
    path('genres/<int:id>/', views.view_genre, name='view_genre'), 
    #path('movies/', views.view_movies, name='view_movies'), 
    path('movies/<int:id>/', views.view_movie, name='view_movie'), 
    path('index_admin/', views.index_admin, name='index_admin'),   
    path('genres/create/', views.form_create_genre, name='form_create_genre'), 
    path('genres/create/post/', views.post_create_genre, name='post_create_genre'),       	
    path('movies/create/', views.form_create_movie, name='form_create_movie'),
    path('movies/create/post/', views.post_create_movie, name='post_create_movie'),
    path('movies/edit/<int:id>/', views.form_edit_movie, name='form_edit_movie'),
    path('movies/edit/post/<int:id>/', views.post_edit_movie, name='post_edit_movie'),
    path('movies/delete/post/<int:id>/', views.post_delete_movie, name='post_delete_movie'),
    path('register_admin/', views.register_admin, name='register_admin'), 
    path('register/admin', views.form_register_admin, name='form_register_admin'), 

    
]