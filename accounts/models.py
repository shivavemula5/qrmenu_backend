from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

class UserManager(BaseUserManager):
   
    def create_user(self,name,email,dob,password=None):
        if not email:
            raise ValueError("users must have an email address")    
        user = self.model(name=name,email=email,dob=dob)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name,email,dob,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(name=name,email=email,dob=dob,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','dob']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    

