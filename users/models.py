from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    STATUS=(
        ('user','user')
        ('admin','admin')
    )

    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    phone=PhoneNumberField()