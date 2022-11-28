from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=20, null=True,blank=True) 
    image=models.ImageField(upload_to='users',null=True,blank=True)


    def say_hello(self):
        return format(self.username)