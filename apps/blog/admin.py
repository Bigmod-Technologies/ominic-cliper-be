from django.contrib import admin
from .models import Blog, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'upload_time', 'writer', 'updated_at')
    search_fields = ('title', 'writer')
    list_filter = ('status', 'upload_time', 'writer')


admin.site.register(Tag)
