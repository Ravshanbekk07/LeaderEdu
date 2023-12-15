from django.shortcuts import render,get_object_or_404
from .models import Results
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResultSerializer,ResultSerializerUZ,ResultSerializerRU
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def check_user(role):
    if role!='admin':
        raise PermissionDenied(detail='Only admins are allowed')

class ResultList(APIView):
    def get(self,request):
        language=request.GET.get('language','ru')
        if language =='uz':
            results=Results.objects.all()
            serializer=ResultSerializerUZ(results,many=True)
            return Response(serializer.data)
        elif language=='ru':
            results=Results.objects.all()
            serializer=ResultSerializerRU(results,many=True)
            return Response(serializer.data)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class ResultCreate(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[JWTAuthentication]
    def post(self,request):
        check_user(request.user.role)
        serializer=ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class ResultDetail(APIView):
    def get(self,request,pk):  
        language=request.GET.get('language','ru')
        if language =='uz':
            result=get_object_or_404(Results,id=pk)
        
            serializer=ResultSerializerUZ(result)
            return Response(serializer.data)
        elif language=='ru':
            result=get_object_or_404(Results,id=pk)
        
            serializer=ResultSerializerRU(result)
            return Response(serializer.data)
        else:
            return Response({'language forbidden'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class ResultUpdate(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[JWTAuthentication]
    def put(self,request,pk):
        check_user(request.user.role)
        result=get_object_or_404(Results,id=pk)
        serializer=ResultSerializer(instance=result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class ResultDelete(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[JWTAuthentication]
    def delete(self,request,pk):
        check_user(role=request.user.role)
        result=get_object_or_404(Results,id=pk)
        result.delete()
        return Response({"status":'Deleted'})
    




        











