from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GenreChoice(models.TextChoices):
    POP = 'POP', 'Pop'
    ROCK = 'RK', 'Rock'
    JAZZ = 'JZ', 'Jazz'
    CLASSIC = 'CL', 'Classic'


class Disk(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=3, choices=GenreChoice.choices, default=GenreChoice.CLASSIC)
    title = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.pk:  # Только для создания, не редактирования
            self.author = self.request.user
        super().save(*args, **kwargs)
