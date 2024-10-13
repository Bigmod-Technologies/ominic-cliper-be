from django.db import models
from django_resized import ResizedImageField
from autoslug import AutoSlugField
import uuid


# Create your models here.


class Price(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        null=True,
        default=None,
        always_update=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = ResizedImageField(
        upload_to="Price/cover_image/", quality=75, force_format="WEBP"
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
