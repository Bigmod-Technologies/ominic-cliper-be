from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'price', 'short_description', 'created_at', 'updated_at')
    search_fields = ('service_title', 'short_description')
    list_filter = ('created_at', 'updated_at')
