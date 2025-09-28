from django.db import models
from Library_BookStore.models import *

# Create your models here.
class LibraryUsers(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.IntegerField()
    
    
class UserBooks(models.Model):
    user_email = models.ForeignKey(LibraryUsers, on_delete=models.CASCADE)
    book_title = models.ForeignKey(BooksAutors_Names, on_delete=models.CASCADE)
    book_name = models.ForeignKey(BooksNames, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)