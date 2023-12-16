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
        fields=[]
class EnrolmentSerializerRu(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=[]