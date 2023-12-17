from users.models import CustomUser
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['name','password','email']
        extra_kwargs=({'password':{'write_only':True}})

    def create(self,validated_data):
        user=CustomUser(
            name=validated_data['name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    name=serializers.CharField()
    password=serializers.CharField()