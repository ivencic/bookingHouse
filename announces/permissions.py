from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsActiveOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_active:
            return True
        return obj.owner == request.user


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit or delete it.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user