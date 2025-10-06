from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
# class UsersAdmin(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     password = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True) 
    
# class UsersColaborators(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     password = models.IntegerField()
#     created_by = models.ForeignKey(UsersAdmin, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    

# class AdminUsers(AbstractUser):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     password = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

class CustomUserManager(UserManager):
    def __create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a value email")
        
        email = self.normalize_email(email)
        user = self.model(username = username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        
        return user
    
    def create_user(self, username = None,  email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.__create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username = None, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.__create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, blank=True, default='', unique=True)
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=150, blank=True, default='')
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    data_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = 'User',
        verbose_name_plural = 'Users'
        
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]