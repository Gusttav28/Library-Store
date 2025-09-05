from django.db import models

# Create your models here.
class BooksAutors_Names(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class BooksNames(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(BooksAutors_Names, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
class BooksNew_Orders(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(BooksAutors_Names, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    