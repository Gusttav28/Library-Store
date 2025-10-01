from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class UsersAdmin(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class UsersColaborators(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    created_by = models.ForeignKey(UsersAdmin, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

class AdminUsers(AbstractUser):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
