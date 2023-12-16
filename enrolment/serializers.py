from rest_framework import serializers
from .models import Enrolment

class Enrolmenterializer(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields="__all__"

class EnrolmentSerializerUz(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=[]
class EnrolmentSerializerRu(serializers.ModelSerializer):
    class Meta:
        model=Enrolment
        fields=[]