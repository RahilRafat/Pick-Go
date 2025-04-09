from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsRestaurantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner_fk or request.user.is_staff

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners or staff to update restaurants.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user == obj.owner_fk or request.user.is_staff
