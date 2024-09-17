from django.contrib import admin
from version.models import Version


# Register your models here.

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "is_active",)
    list_filter = ("version_name", "is_active",)
    search_fields = ("version_name", "version_number",)
