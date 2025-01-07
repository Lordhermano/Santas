from django.db import models
from .forms import Register

# Create your models here.
class Createaccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=400)
    date_of_birth = models.CharField(max_length=200)