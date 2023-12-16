from django.db import models
from teachers.models import Teacher

class Courses(models.Model):
    course_name_uz=models.CharField(max_length=100)
    course_name_ru=models.CharField(max_length=100)

    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    duration_uz=models.CharField(max_length=50)
    duration_ru=models.CharField(max_length=50)

    students_number=models.IntegerField()
    price=models.FloatField(max_length=20)

    lectures_uz=models.CharField(max_length=30)
    lectures_ru=models.CharField(max_length=30)
    
    picture=models.ImageField(upload_to='pictures',null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.course_name_uz} {self.teacher}"
    
class Category(models.Model):
    type_uz=models.CharField(max_length=100)
    type_ru=models.CharField(max_length=100)
    description_uz=models.CharField()
    description_ru=models.CharField()
    picture =models.ImageField(upload_to='pictures/',null=True,blank=True)
    

    def __str__(self) -> str:
        return f'{self.type_uz}  {self.description_uz}'
