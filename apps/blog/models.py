from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    blog_slug = AutoSlugField(
        populate_from="title", unique=True, null=True, default=None
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    upload_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField()
    tag = models.ManyToManyField(Tag)
    thumbnails = ResizedImageField(
        upload_to="Blog/thumbnails", quality=75, force_format="WEBP"
    )
    blog_details = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
