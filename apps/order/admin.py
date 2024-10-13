from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "name", "email", "service")
    search_fields = ("order_id",)
