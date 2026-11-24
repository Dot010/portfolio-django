from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "status", "criado_em")
    list_filter = ("status",)
    search_fields = ("titulo", "corpo")
    prepopulated_fields = {"slug": ("titulo",)}