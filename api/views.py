from rest_framework import filters, viewsets
from rest_framework.permissions import IsAdminUser

from api.models import User
from api.permissions import ReadOnly
from api.serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Класс, работающий с профилями пользователей"""
    queryset = User.objects.all()
    permission_classes = (IsAdminUser | ReadOnly,)

    def get_serializer_class(self):
        """Выбирает сериализатор в зависимости от задачи"""
        if self.action in ('create', 'update', 'partial_update'):
            return WriteOnlyUserSerializer
        return ReadOnlyUserSerializer
