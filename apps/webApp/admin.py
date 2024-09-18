from django.contrib import admin
from .models import PricingImage, Portfolio, PortfolioExampleImage


@admin.register(PricingImage)
class PricingImageAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_image', 'product_price', 'created_at', 'updated_at')
    search_fields = ('image', 'product_title')
    list_filter = ('product_title', 'created_at', 'updated_at')


class PortfolioExampleImageInline(admin.TabularInline):
    model = PortfolioExampleImage
    extra = 1  # Allows adding more images in the admin panel


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_title', 'portfolio_description')
    inlines = [PortfolioExampleImageInline]  # Display example images inline


# Register your models here.
