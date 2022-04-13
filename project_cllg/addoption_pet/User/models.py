from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from django.db.models.fields.files import ImageField

# def get_profile_image_filepath(self,filename):
#     return f'profile_image/{self.pk}/{"profile_image.png"}'

# def get_default_image_filepath(self,filename):
#     return f'#'


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email', max_length=254,unique=True)
    username = models.CharField( max_length=50,unique=True)
    date_joined = models.DateTimeField( verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField( verbose_name="last login",auto_now=True )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']
    
    def __str__(self):
        return self.username
    

