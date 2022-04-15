from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)


class Comment(models.Model):
    vote = models.ForeignKey(
        Vote, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.CharField(null=True, max_length=200)
    pick = models.CharField(null=True, max_length=30)