from django.shortcuts import *

# Create your views here.

def HomeView(request):
    return render(request, "home.html")

def BookStore(request):
    return render(request, "BookStore.html")

def AdminSite(request):
    return render(request, "AdminSite.html")