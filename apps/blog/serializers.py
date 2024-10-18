# serializer
from rest_framework import serializers


# models
from .models import Blog, Tag
from django.contrib.auth.models import User


class BlogTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
        }


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {
            "title": {"required": True},
            "blog_slug": {"read_only": True},
            "writer": {"read_only": True},
            "short_description": {"required": True},
            "thumbnails": {"required": True},
            "blog_details": {"required": True},
        }


class WriterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class BlogDetailsSerializers(serializers.ModelSerializer):
    writer = WriterSerializers()
 

    class Meta:
        model = Blog
        fields = "__all__"
