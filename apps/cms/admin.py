from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Metadata


@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ("key", "title", "description", "keywords")
