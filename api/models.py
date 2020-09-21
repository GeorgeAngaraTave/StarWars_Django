from django.db import models

# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    history_of = models.CharField(max_length=100)
    opening_text = models.TextField()
    release_date = models.DateField()
    add_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.director, self.opening_text, self.release_date)


class Planet(models.Model):
    name = models.CharField(max_length = 80)
    description = models.CharField(max_length=100)
    movie_planet = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'planet'
        verbose_name_plural = 'planets'

    def __str__(self):
        return "{} {} {}".format(self.name, self.description, self.movie_planet)


class Pharacter(models.Model):
    name = models.CharField(max_length = 150)
    add_date = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'character'
        verbose_name_plural = 'pharacters'
        
class MoviePharacter(models.Model):
    pharacters = models.ForeignKey(Pharacter, on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 

    def __str__(self):
        return self.pharacters

    class Meta:
        verbose_name = 'MoviePharacter'
        verbose_name_plural = 'MoviePharacters'    
