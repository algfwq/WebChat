from django.db import models

# Create your models here.
class Settings(models.Model):
    web_name = models.CharField(max_length=100,default='WebChat')
    email_ture = models.CharField(max_length=5,default='T')

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100,default='NO')
    super = models.CharField(max_length=10,default='F')
    robot = models.CharField(max_length=10,default='F')