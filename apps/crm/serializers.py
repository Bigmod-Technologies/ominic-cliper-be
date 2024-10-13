# serializer
from rest_framework import serializers

# models
from .models import ContactMessage


class ContactMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "email": {"required": True},
            "message": {"required": True},
            "site": {"required": False},
        }
