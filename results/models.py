from django.db import models
from teachers.models import Teacher

class Results(models.Model):
    description_uz=models.CharField(max_length=500)
    description_ru=models.CharField(max_length=500)
    picture=models.ImageField(upload_to='pictures',null=True,blank=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.teacher)