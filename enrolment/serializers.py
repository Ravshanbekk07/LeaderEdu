from rest_framework import serializers
from .models import Enrolment

class Enrolmenterializer(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields="__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_id'] = instance.courses.all()
        return representation

class EnrolmentSerializerUz(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=['id','name_uz','age','student_number','parents_number','course_language_uz','course_id','status']
class EnrolmentSerializerRu(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=['id','name_ru','age','student_number','parents_number','course_language_ru','course_id','status']