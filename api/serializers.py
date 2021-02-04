from api.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    """Сериализатор для показа профиля пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser',)
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True},
            'last_login': {'read_only': True},
            'is_superuser': {'read_only': True}
        }


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания, изменения и удаления профиля пользователя"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active',)
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True},
            'password': {'required': True}
        }

    def validate_password(self, value: str) -> str:
        return make_password(value)
