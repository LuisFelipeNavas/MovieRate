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
    path('cat/badmoms.html/', views.badmoms, name='cat/badmoms'), 
    path('cat/ranking.html/', views.ranking, name='cat/ranking'),
]