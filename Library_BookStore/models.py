from django.db import models

# Create your models here.
class BooksAutors_Names(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class BooksNames(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(BooksAutors_Names, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class BooksNew_Orders(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(BooksAutors_Names, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # author = BooksAutors_Names.objects.get(id = 2)
    # boook = BooksNames.objects.create(title='Daniel', author=author, gender = 'test-horror', category = 'horror-history')
    # filterting = BooksNames.objects.filter(author_id = 1).values('title', 'author', 'category', 'gender')
    # print(BooksNames.objects.filter(author_id = 10).values('title', 'author__name', 'category', 'gender'))