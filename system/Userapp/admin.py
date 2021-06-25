from django.contrib import admin
from .models import *


# Register your models here.
class AdminPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class ManagerPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class StaffPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


admin.site.register(Admin, AdminPermission)
admin.site.register(Manager, ManagerPermission)
admin.site.register(Staff, StaffPermission)
