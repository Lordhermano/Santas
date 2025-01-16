from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)


class Createaccount(AbstractBaseUser,PermissionsMixin):

    choice = [
         ('Standard','Standard'),
         ('Premium','Premium'),
         ('VIP','VIP')
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    account = models.CharField(max_length=200,choices=choice,default='Standard')
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=200)

    # Necessary
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    # Necesarry
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['name', 'account', 'date_of_birth']

    # Making it presentable
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def get_full_name(self):
            return self.name
    def get_short_name(self):
            return self.name or self.email.split('@')[0]
class Trips(models.Model):
    title = models.CharField(max_length=200)
    item_des = models.CharField(max_length=100)
    item_price = models.FloatField(max_length=100)
              
class Destination(models.Model):

     name = models.CharField(max_length=200)
     img = models.ImageField(upload_to="images")
     desc = models.TextField()
     adult_price = models.IntegerField()
     child_price = models.IntegerField()
     infant_price = models.IntegerField()          
