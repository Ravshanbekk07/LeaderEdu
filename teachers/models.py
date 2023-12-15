from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Teacher(models.Model):
    name_uz=models.CharField(max_length=100)
    name_ru=models.CharField(max_length=100)

    description_uz=models.CharField(null=True,blank=True)
    description_ru=models.CharField(null=True,blank=True)

    phone=PhoneNumberField()
    experience_uz=models.CharField(max_length=50)
    experience_ru=models.CharField(max_length=50)
    score=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pictures',null=True,blank=True)

    def __str__(self) -> str:
        return self.name_uz