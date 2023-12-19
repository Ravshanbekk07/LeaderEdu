from django.shortcuts import render,get_object_or_404
from rest_framework.exceptions import PermissionDenied
from .serializers import (CourseSerializer,CategorySerializer,CategorySerializerRU,CategorySerializerUZ,
CourseSerializerRU,CourseSerializerUZ)
from rest_framework.views import APIView
from .models import Courses,Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def check_user(role):
    if role != "admin":
        raise PermissionDenied(detail='Only admins are allowed')

class CourseList(APIView):
    def get(self,request):
        language=request.GET.get('language','ru')
        if language =='uz':
            courses=Courses.objects.all()
            serializer=CourseSerializerUZ(courses,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            courses=Courses.objects.all()
            serializer=CourseSerializerRU(courses,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class CourseCreate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        check_user(request.user.role)
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CourseDetail(APIView):
    def get(self,request,pk):  
        language=request.GET.get('language','ru')
        if language =='uz':
            course=get_object_or_404(Courses,id=pk)
        
            serializer=CourseSerializerUZ(course)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            course=get_object_or_404(Courses,id=pk)
        
            serializer=CourseSerializerRU(course)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class CourseUpdate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def put(self,request,pk):
        check_user(request.user.role)
        result=get_object_or_404(Courses,id=pk)
        serializer=CourseSerializer(instance=result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CourseDelete(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def delete(self,request,pk):
        check_user(role=request.user.role)
        result=get_object_or_404(Courses,id=pk)
        result.delete()
        return Response({"status":'Deleted'},status=status.HTTP_200_OK)

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
class CategoryCreate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        check_user(request.user.role)
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CategoryDetail(APIView):
    def get(self,request,pk):  
        language=request.GET.get('language','ru')
        if language =='uz':
            category=get_object_or_404(Category,id=pk)
            serializer=CategorySerializerUZ(category)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            category=get_object_or_404(Category,id=pk)
            serializer=CategorySerializerRU(category)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class CategoryUpdate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def put(self,request,pk):
        check_user(request.user.role)
        category=get_object_or_404(Category,id=pk)
        serializer=CourseSerializer(instance=category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
class CategoryDelete(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def delete(self,request,pk):
        check_user(role=request.user.role)
        category=get_object_or_404(Category,id=pk)
        category.delete()
        return Response({"status":'Deleted'},status=status.HTTP_200_OK)
        