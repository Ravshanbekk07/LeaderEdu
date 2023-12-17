from django.shortcuts import render
from .serializers import TokenSerializer,Registerserializer,LoginSerializer
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import permissions
from django.contrib.auth import logout

class ObtainTokenView(APIView):
    def post(self,request):
        serializer=TokenSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            try:
                user=CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self,request):
        serializer=Registerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                refresh=RefreshToken.for_user(user)
                return Response({ 'refresh': str(refresh),'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        try:
            logout(request)
            return Response({'detail': 'Logout successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Unable to logout'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

