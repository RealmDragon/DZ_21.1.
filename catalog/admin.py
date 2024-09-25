from django.contrib import admin
from catalog.models import Product, Category, Version
from django.contrib.auth.admin import UserAdmin

# Регистрация модели User с дополнительными полями
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        *UserAdmin.fieldsets,  # Стандартные поля пользователя
        (
            'Дополнительная информация',  # Заголовок секции
            {
                'fields': ('avatar', 'phone_number', 'country'),
            }
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_filter = ("name",)
    search_fields = ("name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at", "owner")
    list_filter = ("category", "owner")
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "version_number", "version_name", "is_current")
    list_filter = ("product", "is_current")
    search_fields = ("product__name", "version_name")
    actions = ["set_current_version"]

    def set_current_version(self, request, queryset):
        # Убедитесь, что выбрана только одна версия
        if queryset.count() != 1:
            self.message_user(request, "Выберите только одну версию для установки как текущую.")
            return

        version = queryset.first()
        if version.is_current:
            self.message_user(request, "Эта версия уже установлена как текущая.")
            return

        version.set_current_version()
        self.message_user(request, "Версия установлена как текущая.")

    set_current_version.short_description = "Установить как текущую версию"