from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # First check if the user is a superuser
        if request.user and request.user.is_superuser:
            return True
            
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # First check if the user is a superuser
        if request.user and request.user.is_superuser:
            return True
            
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user