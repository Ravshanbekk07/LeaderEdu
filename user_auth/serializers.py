from users.models import CustomUser
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)