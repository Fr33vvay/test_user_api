from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает работать с объектом только его владельцу
    """
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.id == request.user.id
