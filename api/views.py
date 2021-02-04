from api.models import User
from api.permissions import IsOwnerOrReadOnly
from api.serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """Класс, работающий с профилями пользователей"""
    queryset = User.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name', ]
    ordering_fields = ['username']

    def get_serializer_class(self):
        """Выбирает сериализатор в зависимости от задачи"""
        if self.action in ('create', 'update', 'partial_update', 'destroy',):
            return WriteOnlyUserSerializer
        return ReadOnlyUserSerializer

    def get_permissions(self):
        """
        Пользователи могут создавать профили других пользователей,
        но не удалять или изменять их
        """
        if self.action in ('update', 'partial_update', 'destroy',):
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
