from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    order = models.CharField(max_length=100000000)
    super = models.CharField(max_length=10)