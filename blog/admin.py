from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "slug", "published", "views",)
    list_filter = ("published",)
    search_fields = (
        "title",
        "content",
    )