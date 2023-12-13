from django.shortcuts import render,get_object_or_404
from rest_framework.exceptions import PermissionDenied
from .serializers import CourseSerializer,CategorySerializer,CategorySerializerRU,CategorySerializerUZ
from rest_framework.views import APIView
from .models import Courses,Category
from rest_framework.response import Response

def check_user(role):
    if role != "admin":
        raise PermissionDenied(detail='Only admins are allowed')

class CourseList(APIView):
    def get(self,request):
        courses=Courses.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        check_user(request.user.role)
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CategoryList(APIView):
    def get(self,request):
        language=request.GET.get('language','ru')
        if language == 'uz':
            categories=Category.objects.all()
        
            serializer=CategorySerializerUZ(categories,many=True)
            return Response(serializer.data)
        elif language =='ru':
            categories=Category.objects.all()
        
            serializer=CategorySerializerRU(categories,many=True)
            return Response(serializer.data)

    def post(self,request):
        check_user(request.user.role)
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class CategoryDelete(APIView):
    def delete(self,request,pk):
        check_user(role=request.user.role)
        teacher=get_object_or_404(Category,id=pk)
        teacher.delete()
        return Response({"status":'Deleted'})
        