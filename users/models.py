from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=66)
