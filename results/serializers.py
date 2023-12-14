from rest_framework import serializers
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer
from .models import Results

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Results
        fields="__all__"
    # def to_representation(self, instance):
    #     representation= super().to_representation(instance)
    #     if instance.teacher:
    #         representation['teacher_detail']=TeacherSerializer(instance.teacher).data
    #     return representation
class ResultSerializerUZ(serializers.ModelSerializer):
   
    class Meta:
        model=Results
        fields=['id','description_uz','picture','teacher']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.teacher:
            representation['teacher_detail'] = TeacherSerializer(instance.teacher).data
        return representation

class ResultSerializerRU(serializers.ModelSerializer):
    class Meta:
        model=Results
        fields=['id','description_ru','picture','teacher']
        