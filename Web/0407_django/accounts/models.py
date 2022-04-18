from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

# settings.py => AUTH_USER_MODEL = 'accounts.User'