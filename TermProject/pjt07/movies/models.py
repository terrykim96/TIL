from tkinter import CASCADE
from django.db import models
from pjt07.settings import AUTH_USER_MODEL


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    poster_url = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null = True
    )