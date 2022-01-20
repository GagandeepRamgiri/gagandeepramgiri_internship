from pyexpat import model
from django.db import models

# Create your models here.

class crud(models.Model):
    uname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
