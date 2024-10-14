from django.contrib import admin
from .models import Price, Sample, SmapleMedia


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "status")


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(SmapleMedia)
class SmapleMediaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sample",
    )
