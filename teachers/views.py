from django.shortcuts import render,get_object_or_404
from .models import Teacher
from rest_framework.permissions import IsAuthenticated
from .serializers import TeacherSerializer,TeacherSerializerUZ,TeacherSerializerRU
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

def check_user(role):
    if role!='admin':
        raise PermissionDenied(detail='Only admins are allowed')
    
class TeacherList(APIView):
    def get(self,request):
        language=request.GET.get('language','ru')
        if language=='uz':
            teachers=Teacher.objects.all()
            serializer=TeacherSerializerUZ(teachers,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            teachers=Teacher.objects.all()
            serializer=TeacherSerializerRU(teachers,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'error':'Language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class TeacherCreateView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        
            check_user(role=request.user.role)
            serializer=TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class TeacherDetail(APIView):
   
    def get(self,request,pk):
        language=request.GET.get('language','ru')
        if language=='uz':
            teacher=get_object_or_404(Teacher,id=pk)
            serializer=TeacherSerializerUZ(teacher)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            teacher=get_object_or_404(Teacher,id=pk)
            serializer=TeacherSerializerRU(teacher)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'error':'Language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class TeacherUpdate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def put(self,request,pk):
        check_user(request.user.role)
        teacher=get_object_or_404(Teacher,id=pk)
        serializer=TeacherSerializer(instance=teacher,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TeacherDelete(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def delete(self,request,pk):
        check_user(role=request.user.role)
        teacher=get_object_or_404(Teacher,id=pk)
        teacher.delete()
        return Response({"status":'Deleted'},status=status.HTTP_200_OK)
    
class TeacherSearch(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        check_user(role=request.user.role)

        name_uz=request.GET.get('name','')
        teacher=Teacher.objects.filter(name_uz__icontains=name_uz)
        serializer=TeacherSerializer(teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        



        





