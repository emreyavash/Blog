from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
     
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )
        return self.create_user(email,password,**extra_fields)

    

    

class CustomUser(AbstractUser,PermissionsMixin):
    username =None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.BooleanField(null=True)
    profil_image = models.ImageField(upload_to='writers',null=True)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    birthday= models.DateField(null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    def __str__(self):
        return self.email