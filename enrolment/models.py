from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from courses.models import Courses
from django.core.validators import MaxValueValidator

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

    age=models.IntegerField(validators=[MaxValueValidator(100)])
    student_numer=PhoneNumberField()
    parents_numer=PhoneNumberField()

    course_language_uz=models.CharField(max_length=30,choices=Language_uz)
    course_language_ru=models.CharField(max_length=30,choices=Language_ru)
    status=models.CharField(max_length=50,choices=STATUS,default='New')
    course_id=models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name_uz or self.name_ru
 