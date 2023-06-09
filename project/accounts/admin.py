from constance import config
from django.contrib import admin

from project.accounts.models import FunctionalPermission, User

admin.site.site_header = f"{config.INSTANCE_TITLE} configuration"

admin.site.register(User)


@admin.register(FunctionalPermission)
class FunctionalPermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "module")
    search_fields = ("name", "codename", "module")
    list_filter = ("module",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
