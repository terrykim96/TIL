from django.db import models
from django import forms

# Create your models here.
class Movie(models.Model):

    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre_choice = (('공포', '공포'), ('코미디', '코미디'), ('로맨스', '로맨스'))
    genre = models.CharField(max_length=30, choices=genre_choice)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()