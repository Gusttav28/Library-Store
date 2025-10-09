from django.shortcuts import *
from .models import *
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def HomeView(request):
    return render(request, "home.html")



def BookStore(request):
    gettingBooks = BooksNames.objects.values('title', 'author', 'category', 'gender')
    gettingBooksList = list(BooksNames.objects.values('title', 'author', 'category', 'gender'))
    # data = serializers.serialize('json', gettingBooks)
    data = JsonResponse(gettingBooksList, safe=False)
    context = {
        'getInfo':'Getting Books Successfully',
        'request_status': data,
        'title':BooksNames.objects.values('title'),
        'author':BooksNames.objects.values('author'),
        'category':BooksNames.objects.values('category'),
        'gender':BooksNames.objects.values('gender'),
    }
    print()
    for i in context['title']:
        print(i)
        
    for i in gettingBooks:
        print(i)
    return render(request, 'BookStore.html', context)


def AdminSite(request):
    return render(request, "AdminSite.html")