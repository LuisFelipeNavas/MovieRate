from django.db import models
from django.contrib.auth.models import User	

class Movie(models.Model):
    title = models.CharField(max_length=200, null=False)   
    sinopsis = models.TextField(max_length=2000, null=True)
    year = models.IntegerField(null=True)
    cast = models.TextField(max_length=2000, null=True)
    duration = models.IntegerField(null=False)
    trailer = models.CharField(max_length=100, null=False)   
    onBillboard = models.BooleanField(null=False)

    def __str__(self):
        return self.title
        
    class Meta:
        app_label = 'app'

class Genre(models.Model):
    name = models.CharField(max_length=45, null=False)
    movies = models.ManyToManyField(Movie, related_name='movies')

    def __str__(self):
        return self.name
        
    class Meta:
        app_label = 'app'

class Score(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(User,
                  related_name='user_score',
                  null=False,                  
                  on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,
                  related_name='movie_score',
                  null=False,                  
                  on_delete=models.PROTECT)        
    
    def __str__(self):
        return self.value

    class Meta:
        app_label = 'app'

class Comment(models.Model):
    text = models.TextField(max_length=200, null=False)
    dateHour = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(null=False)
    user = models.ForeignKey(User,
                  related_name='user_comment',
                  null=False,                  
                  on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,
                  related_name='movie_comment',
                  null=False,                  
                  on_delete=models.PROTECT)        
    
    def __str__(self):
        return self.text

    class Meta:
        app_label = 'app'