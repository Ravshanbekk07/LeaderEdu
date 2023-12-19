from django.shortcuts import render
from .serializers import TokenSerializer,Registerserializer,LoginSerializer,PasswordChangeSerializer#,GoogleSignupSerializer
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import permissions
from django.contrib.auth import logout
from social_django.models import UserSocialAuth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'login.html')
@login_required
def home(request):
    return render(request,'home.html')

# class GoogleSignUp(APIView):
#     def post(self, request):
#         serializer = GoogleSignupSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

       
#         user, created = CustomUser.objects.get_or_create(
#             email=email,
#             defaults={'username': username},
#         )

#         if not created:
#             return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

   
#         user.set_password(password)
#         user.save()

       
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)


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

class PasswordChange(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        user=request.user
        serializer=PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            old_password=serializer.validated_data['old_password']
            new_password=serializer.validated_data['new_password']
            if not user.check_password(old_password):
                return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    