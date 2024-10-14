# serializer
from rest_framework import serializers


# models
from .models import Price, SmapleMedia, Sample


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


class SampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"
        extra_kwargs = {
            "title": {"required": True},
            "description": {"required": True},
            "image1": {"required": True},
            "image2": {"required": True},
        }


class SmapleMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = SmapleMedia
        fields = "__all__"
        extra_kwargs = {
            "sample": {"read_only": True},
            "media": {"required": True},
        }
