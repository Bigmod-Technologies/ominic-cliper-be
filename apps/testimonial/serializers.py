# serializer
from rest_framework import serializers

# models
from .models import ClientTestimonial


class ClientTestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientTestimonial
        fields = "__all__"
        extra_kwargs = {
            "service_title": {"required": True},
            "client_name": {"required": True},
            "client_designation": {"required": True},
            "review": {"required": True},
            "image": {"required": True},
        }
