from django.db import models

# Create your models here.
class user (models.Model):
    first_name=models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)