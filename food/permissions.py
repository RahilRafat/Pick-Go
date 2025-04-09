from rest_framework.permissions import BasePermission

class IsFoodOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        
        if request.user.is_staff:
            return True
        
        return obj.res_fk.owner_fk == request.user
