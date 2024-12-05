# serializer
from rest_framework import serializers

# models

from .models import Service


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        extra_kwargs = {
            "service_title": {"required": True},
            "service_slug": {"read_only": True},
            "price": {"required": True},
            "short_description": {"required": True},
            "details_text_editor": {"required": True},
            "cover_image": {"required": True},
            
        }
