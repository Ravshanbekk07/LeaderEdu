from django.db import models
from teachers.models import Teacher

class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    duration=models.CharField(max_length=50)
    students_number=models.IntegerField()
    price=models.FloatField(max_length=20)
    lectures=models.CharField(max_length=30)
    picture=models.ImageField(upload_to='pictures',null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.course_name} {self.teacher}'