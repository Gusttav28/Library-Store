from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('signin/', views.SignInView, name='signin'),
    path('userSettings/', views.userSettings, name='usersettings'),
    path('userBooks/', views.userBooks, name='userbooks'),
    path('loginout/', views.LogOut, name='loginout'),
]
