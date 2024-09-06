# users/permissions.py
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):


    def has_permission(self, request, view):
        # Only allow authenticated users with admin status to create owners
        if request.method == 'POST' and view.__class__.__name__ == 'SignUpView':
            return request.user and request.user.is_authenticated and request.user.is_staff
        return True
