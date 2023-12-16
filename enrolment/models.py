from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Enrolment(models.Model):
    STATUS=(
        ('New','New'),
        ('Disagreement','Disagreement'),
        ('Agreement','Agreement')
    )
    Language_uz = (
        ("O'zbek","O'zbek"),
        ("Rus","Rus")
    )

    Language_ru = (
        ("Узбек","Узбек"),
        ("Русский","Русский")
    )
    name_uz=models.CharField(max_length=100)
    name_ru=models.CharField(max_length=100)

    age=models.IntegerField(max_length=2)
    student_numer=PhoneNumberField()
    parents_numer=PhoneNumberField()

    course_language_uz=models.CharField(max_length=30,choices=Language_uz,default="O'zbek")
    course_language_ru=models.CharField(max_length=30,choices=Language_ru,default="Русский")
    status=models.CharField(max_length=50,choices=STATUS,default='New')
    

