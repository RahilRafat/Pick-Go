# permissions.py
from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is staff (admin) and authenticated
        return request.user  and request.user.is_staff




class IsOwnerUser(BasePermission):
     def has_object_permission(self, request, view, obj):
        # Check if the user is the owner or admin
        return request.user == obj.owner_fk or request.user.is_staff
    



class IsCustomUser(BasePermission):
    """
    Permission to allow CustomUsers to retrieve all restaurants.
    """

    def has_permission(self, request, view):
        if request.user :
            # Deny owners from accessing the list of all restaurants
            if view.action == 'list' and request.user.is_owner:
                return False
            return True
        return False
        
        
    
