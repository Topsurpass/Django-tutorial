from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        # Hash the password before saving the user instance
        password = validated_data.pop('password', None)
        if password:
            user = User.objects.create(**validated_data)
            user.set_password(password)  # Hash the password
            user.save()
            return user
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
