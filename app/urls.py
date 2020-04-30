from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    
    path('login/', views.log_in, name='log_in'), 
    path('register/', views.register, name='register'), 
    path('base/', views.base, name='base'), 
    path('prueba/', views.prueba, name='prueba'), 
    path('cat/', views.cat, name='cat'), 
    path('badmoms/', views.badmoms, name='badmoms'), 
    path('ranking/', views.ranking, name='ranking'),
    path('movielist/', views.movie_list, name='movie_list'),
]