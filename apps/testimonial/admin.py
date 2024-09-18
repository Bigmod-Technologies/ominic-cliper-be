from django.contrib import admin
from .models import ClientTestimonial


@admin.register(ClientTestimonial)
class ClientTestimonialAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'client_name', 'client_designation',)
    search_fields = ('service_title', 'client_name')
  



