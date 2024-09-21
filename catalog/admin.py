from django.contrib import admin
from catalog.models import Product, Category, Version



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_filter = ("name",)
    search_fields = ("name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at",)
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "version_number", "version_name", "is_current")
    list_filter = ("product", "is_current")
    search_fields = ("product__name", "version_name")
    actions = ["set_current_version"]

    def set_current_version(self, request, queryset):
        for version in queryset:
            version.set_current_version()
        self.message_user(request, "Версия установлена как текущая.")

    set_current_version.short_description = "Установить как текущую версию"
