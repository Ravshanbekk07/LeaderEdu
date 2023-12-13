from rest_framework import serializers
from .models import Category,Courses
from teachers.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=['id','course_name','teacher','duration','students_number','price','lectures','picture']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.teacher:
            representation['teacher_detail'] = TeacherSerializer(instance.teacher).data
        return representation


class CategorySerializerRU(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','type_ru', 'description_ru', 'picture']

class CategorySerializerUZ(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','type_uz', 'description_uz', 'picture']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__' 

   
   