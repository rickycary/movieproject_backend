from django.db import models

# Create your models here.
class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    poster = models.CharField(max_length=100)