from users.models import CustomUser
from rest_framework import serializers
from social_django.models import UserSocialAuth

# class GoogleSignupSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
        
class SocialAccessTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()

class TokenSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email']
        extra_kwargs=({'password':{'write_only':True}})
    
    
    def create(self,validated_data):
            if len(validated_data['password']) < 8:
                raise serializers.ValidationError("Password must be at least 8 characters long.")
            else:
                user=CustomUser(
                    username=validated_data['username'],
                    email=validated_data['email'],
                )
                user.set_password(validated_data['password'])
                user.save()
                return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

class PasswordChangeSerializer(serializers.Serializer):
    old_password=serializers.CharField()
    new_password=serializers.CharField()
