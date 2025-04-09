from rest_framework.permissions import BasePermission

class IsSizeOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
     
        if request.user.is_staff:
            return True
        
        return obj.owner_fk == request.user
