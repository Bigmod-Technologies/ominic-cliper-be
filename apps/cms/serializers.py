# serializer
from rest_framework import serializers

# models

from .models import PageContent


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = "__all__"

    def create(self, validated_data):
        data, created = PageContent.objects.get_or_create(key=validated_data.get("key"))
        data.image = validated_data.get("image")
        data.save()
        return data
