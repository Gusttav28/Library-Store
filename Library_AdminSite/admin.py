from django.contrib import admin
from .models import *
from Library_BookStore.models import *

# Register your models here.

admin.site.site_header = "Library Store Admin Panel"
admin.site.site_title = "Library Store Admin Panel"
admin.site.index_title = "Welcome To Library Admin Panel"

admin.site.register(User)
admin.site.register(BooksNames)
admin.site.register(BooksAutors_Names)
admin.site.register(BooksNew_Orders)