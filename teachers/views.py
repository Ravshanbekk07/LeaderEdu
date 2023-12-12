from django.shortcuts import render,get_object_or_404
from .models import Teacher
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete','destroy']:
            return [IsAdminUser()]
        else:
            return [IsAuthenticatedOrReadOnly()]





