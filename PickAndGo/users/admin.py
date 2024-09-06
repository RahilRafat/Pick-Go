from django.contrib import admin
from .models import Admin, Owner

@admin.register(Admin)
class AdminnAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'admin_fk', 'res_fk')

#     def has_add_permission(self, request):
#         return request.user.has_perm('users.can_create_owner') or request.user.is_superuser
    
# admin.site.register(Adminn, AdminnAdmin)
# admin.site.register(Owner, OwnerAdmin)
