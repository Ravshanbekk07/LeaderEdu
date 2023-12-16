from rest_framework import serializers
from .models import Category,Courses
from teachers.serializers import TeacherSerializer,TeacherSerializerRU,TeacherSerializerUZ


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=['id','course_name_uz','course_name_ru','teacher',
                'duration_uz','duration_ru','students_number',
                'price','lectures_uz','lectures_ru','picture']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.teacher:
            representation['teacher_detail'] = TeacherSerializer(instance.teacher).data
        return representation
    
class CourseSerializerUZ(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=['id','course_name_uz','teacher',
                'duration_uz','students_number',
                'price','lectures_uz','picture']
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        if instance.teacher:
            representation['teacher_detail'] = TeacherSerializerUZ(instance.teacher).data
        return representation
        
class CourseSerializerRU(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=['id','course_name_ru','teacher',
                'duration_ru','students_number',
                'price','lectures_ru','picture']
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        if instance.teacher:
            representation['teacher_detail'] = TeacherSerializerRU(instance.teacher).data
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

   
   