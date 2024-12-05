# serializer
from rest_framework import serializers

# models

from .models import PageContent, Metadata


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = "__all__"

    def create(self, validated_data):
        data, created = PageContent.objects.get_or_create(key=validated_data.get("key"))
        data.image = validated_data.get("image")
        data.save()
        return data


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = "__all__"

    def create(self, validated_data):
        data, created = Metadata.objects.get_or_create(key=validated_data.get("key"))
        data.title = validated_data.get("title")
        data.description = validated_data.get("description")
        data.keywords = validated_data.get("keywords")
        data.save()
        return data
