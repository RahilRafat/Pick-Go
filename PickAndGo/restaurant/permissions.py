# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is staff (admin) and authenticated
        return request.user and request.user.is_authenticated and request.user.is_staff
