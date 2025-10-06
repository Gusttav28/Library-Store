from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Library Store Admin Panel"
admin.site.site_title = "Library Store Admin Panel"
admin.site.index_title = "Welcome To Library Admin Panel"

admin.site.register(User)