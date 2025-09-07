from django.shortcuts import *
from django.http import HttpResponse
from django.views.generic import *
from .models import *
# Create your views here.


def LoginView(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username)
        print(password)
        db_users = LibraryUsers.objects.filter(username = username, password = password).values('name', 'password')
        if db_users:
            print("successfully")
        else:
            print('invalid login')
        print(db_users)
        
        
    return render(request, "login.html")

def SignInView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        test_user = LibraryUsers.objects.filter(email = email).values('email')
        if test_user:
            print("the email provide it exist already")
        else:
            db_users = LibraryUsers(name = name, last_name = last_name, username = user_name, email = email, password = password)
            db_users.save()
            print(LibraryUsers.objects.all().values())
    return render(request, "signin.html")



# class LoginView(View):
#     template_name = "login.html"
#     def get_context_data(self, request, *args, **kwargs):
#         data = request.POST.get("username")
#         return render(request, 'login.html', {'data_received': data})
    
    
# class SignInView(TemplateView):
#     template_name = "signin.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["App Name"] =  "Library Store"
#         return context
    