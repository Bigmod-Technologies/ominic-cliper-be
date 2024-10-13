# serializer
from rest_framework import serializers


# models
from .models import Price


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"
        extra_kwargs = {
            "title": {"required": True},
            "slug": {"read_only": True},
            "price": {"required": True},
            "description": {"required": True},
            "cover_image": {"required": True},
            "status": {"required": True},
        }
