from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Enrolment
from .serializers import Enrolmenterializer,EnrolmentSerializerRU,EnrolmentSerializerUZ
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from courses.models import Courses

def check_user(role):
    if role!='admin':
        raise PermissionDenied(detail='Only admins are allowed')

class EnrolmentList(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        check_user(request.user.role)
        enrolments=Enrolment.objects.all()
        serializer=Enrolmenterializer(enrolments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class EnrolmentDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request,pk):  
        check_user(request.user.role)

        language=request.GET.get('language','ru')
        if language =='uz':
            enrolment=get_object_or_404(Enrolment,id=pk)
        
            serializer=EnrolmentSerializerUZ(enrolment)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif language=='ru':
            enrolment=get_object_or_404(Enrolment,id=pk)
        
            serializer=EnrolmentSerializerRU(enrolment)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class EnrolmentUpdate(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def put(self,request,pk):
        check_user(request.user.role)
        enrolment=get_object_or_404(Enrolment,id=pk)
        serializer=Enrolmenterializer(instance=enrolment,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class EnrolmentDelete(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def delete(self,request,pk):
        check_user(role=request.user.role)
        enrolment=get_object_or_404(Enrolment,id=pk)
        enrolment.delete()
        return Response({"status":'Deleted'},status=status.HTTP_200_OK)
      
class EnrolmentCreate(APIView):
    def post(self,request):
        language=request.GET.get('language','ru')
        if language=='uz':
            serializer=EnrolmentSerializerUZ(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif language=='ru':
            serializer=EnrolmentSerializerRU(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)


     