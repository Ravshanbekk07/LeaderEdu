from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(null=True,blank=True)
    phone=models.CharField(max_length=13)
    experience=models.FloatField()
    score=models.FloatField()
    picture=models.ImageField(upload_to='pictures',null=True,blank=True)



    def __str__(self) -> str:
        return self.name