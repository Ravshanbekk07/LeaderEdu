from django.shortcuts import render
from .serializers import TokenSerializer
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status


class ObtainTokenView(APIView):
    def post(self,request):
        serializer=TokenSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data['name']
            try:
                user=CustomUser.objects.get(name=name)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


