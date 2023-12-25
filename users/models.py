from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    STATUS=(
        ('user','user'),
        ('admin','admin'),
    )

    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    phone=PhoneNumberField()
    role=models.CharField(max_length=30,choices=STATUS,default='user')

    def __str__(self) -> str:
        return self.username