from users.models import CustomUser
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email']
        extra_kwargs=({'password':{'write_only':True}})

    def create(self,validated_data):
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

# class PasswordChangeSerializer(serializers)
