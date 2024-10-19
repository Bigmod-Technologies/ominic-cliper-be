from django.db import models
import uuid
from django_resized import ResizedImageField


# Create your models here.
class PageContent(models.Model):
    CHOICES = [
        ("landing_page_hero_image", "Landing Page Hero Image"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=255, choices=CHOICES)
    text = models.TextField(null=True, blank=True)
    image = ResizedImageField(
        upload_to="PageContent/image",
        quality=75,
        force_format="WEBP",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
