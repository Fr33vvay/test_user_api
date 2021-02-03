from rest_framework import serializers

from api.models import User


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    """Сериализатор дляпоказа профиля пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'lastname', 'is_active', 'last_login', 'is_superuser',)
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
        fields = ('username', 'firstname', 'lastname', 'password', 'is_active',)
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True},
            'password': {'required': True}
        }