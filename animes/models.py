from django.db import models

class Animes(models.Model):
    anime_name = models.CharField(max_length=100)
    anime_genre = models.CharField(max_length=50)
    car_imdb_rate = models.IntegerField()
