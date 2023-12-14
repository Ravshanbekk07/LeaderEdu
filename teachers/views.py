from django.shortcuts import render,get_object_or_404
from .models import Teacher
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import TeacherSerializer,TeacherSerializerUZ,TeacherSerializerRU
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response


def check_user(role):
    if role!='admin':
        raise PermissionDenied(detail='Only admins are allowed')
    
class TeacherList(APIView):

    def get(self,request):
        language=request.GET.get('language','ru')
        if language=='uz':
            teachers=Teacher.objects.all()
            serializer=TeacherSerializerUZ(teachers,many=True)
            return Response(serializer.data)
        elif language=='ru':
            teachers=Teacher.objects.all()
            serializer=TeacherSerializerRU(teachers,many=True)
            return Response(serializer.data)
        
    def post(self,request):
        check_user(role=request.user.role)
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class TeacherDetail(APIView):
    def get(self,request,pk):
        teacher=get_object_or_404(Teacher,id=pk)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self,request,pk):
        check_user(request.user.role)
        teacher=get_object_or_404(Teacher,id=pk)
        serializer=TeacherSerializer(instance=teacher,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk):
        check_user(role=request.user.role)
        teacher=get_object_or_404(Teacher,id=pk)
        teacher.delete()
        return Response({"status":'Deleted'})
        



        





