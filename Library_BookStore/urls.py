from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('BookStore/', views.BookStore, name='bookstore'),
    path('AdminSite/', views.AdminSite, name='admin')
]
