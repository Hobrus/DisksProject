from django.db import models


# Create your models here.


class GenreChoice(models.TextChoices):
    POP = 'POP', 'Pop'
    ROCK = 'RK', 'Rock'
    JAZZ = 'JZ', 'Jazz'
    CLASSIC = 'CL', 'Classic'


class Disk(models.Model):
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=3, choices=GenreChoice.choices, default=GenreChoice.CLASSIC)
    title = models.CharField(max_length=100)
