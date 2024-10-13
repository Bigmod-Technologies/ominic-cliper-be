# serializer
from rest_framework import serializers

# models
from .models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "order_id": {"read_only": True},
            "name": {"required": True},
            "email": {"required": True},
            "url": {"required": False},
            "type": {"required": True},
            "appointment": {"required": True},
            "service": {"required": True},
            "message": {"required": True},
        }
