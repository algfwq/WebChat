from django.db import models

# Create your models here.
class Settings(models.Model):
    email_ture = models.CharField(max_length=5)

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    super = models.CharField(max_length=10)