from rest_framework.permissions import BasePermission

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="viewers").exists()

class IsDev(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="developers").exists()
