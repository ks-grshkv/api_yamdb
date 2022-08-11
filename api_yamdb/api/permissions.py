from rest_framework import permissions

from users.models import Roles


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == Roles.admin  

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:         
            return True   
        return request.user.irole == Roles.admin