from django.db import models

# Create your models here.
class LibraryUsers(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()