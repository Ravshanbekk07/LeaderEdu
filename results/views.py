from django.shortcuts import render,get_object_or_404
from .models import Results
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResultSerializer,ResultSerializerUZ,ResultSerializerRU
from rest_framework.exceptions import PermissionDenied

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
    def post(self,request):
        check_user(request.user.role)
        serializer=ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





