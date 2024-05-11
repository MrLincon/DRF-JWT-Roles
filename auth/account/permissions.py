from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.ADMIN

class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.MANAGER
