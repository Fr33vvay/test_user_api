from django.contrib.auth.hashers import make_password

from api.models import User
from rest_framework import serializers


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    """Сериализатор для показа профиля пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser',)


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
