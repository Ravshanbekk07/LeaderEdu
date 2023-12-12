from rest_framework import serializers
from .models import Category,Courses
from teachers.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.teachers.exists():
            representation['teacher_detail'] = TeacherSerializer(instance.teachers.all(), many=True).data
        return representation
    
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
