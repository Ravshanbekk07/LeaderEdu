from rest_framework import serializers
from .models import Enrolment

class Enrolmenterializer(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields="__all__"

    

class EnrolmentSerializerUZ(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=['id','name_uz','age','student_numer','parents_numer','course_language_uz','course_id','status']
class EnrolmentSerializerRU(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=['id','name_ru','age','student_numer','parents_numer','course_language_ru','course_id','status']