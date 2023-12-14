from .models import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class  Meta:
       model=Teacher
       fields='__all__'
       
class TeacherSerializerUZ(serializers.ModelSerializer):
   
    class Meta:
        model=Teacher
        fields=['id','name_uz','description_uz','phone','experience','score','picture',]

   
class TeacherSerializerRU(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','name_ru','description_ru','phone','experience','score','picture']
       
        
