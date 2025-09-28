from django.shortcuts import *
from django.http import HttpResponse
from django.views.generic import *
from .models import *
from django.template import loader
# Create your views here.

def getUser(username, password):
    db_users = LibraryUsers.objects.filter(username = username, password = password).values('name')
    user_name = ""
    for i in db_users:
        user_name = i['name']
    context = {"user": user_name}
    print("printing the information from the get user page: ",db_users)


def LoginView(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        getUser(username, password)
        db_users = LibraryUsers.objects.filter(username = username, password = password).values('name')
        user_name = ""
        for i in db_users:
            user_name = i['name']
        if db_users.exists():
            context = {
                'successfully_login': 'Successfull Login',
                'authenticated':True,
                'user': user_name,
                }
            print(context)
            return render(request, "home.html", context)  
        else:
            context = {
                "authenticated": False,
            }
            print(context)
            print(db_users)
            
    return render(request, 'login.html')

def LogOut(request):
    context = {
        'authenticated': False,
    }
    return render(request, "loginOut.html", context)


def SignInView(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        test_user = LibraryUsers.objects.filter(email = email).values('email')
        if test_user:
            print("the email provide it exist already")
            context = {
                'email_authentication':True,
                'user_message': "The email provide it exist already, try with another or do you have an account created already?",
            }
            print(context)
            return render(request, 'signin.html', context)
        else:
            db_users = LibraryUsers(name = name, last_name = last_name, username = user_name, email = email, password = password)
            db_users.save()
            print(LibraryUsers.objects.all().values())
            context = {
                'email_authentication':False,
                'user_message': "The account was successfully created!",
            }
            return render(request, 'signin.html', context)

    return render(request, "signin.html")


def userSettings(request):
    return render(request, "userSettings.html")


def userBooks(request):
    return render(request, 'userBooks.html')