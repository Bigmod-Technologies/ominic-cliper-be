from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from autoslug import AutoSlugField
import uuid


# Create your models here.
class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_title = models.CharField(max_length=255)
    service_slug = AutoSlugField(populate_from='service_title', unique=True, null=True, default=None,
                                 always_update=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=255)
    details_text_editor = RichTextField()
    cover_image = ResizedImageField(upload_to='Service/cover_image/', quality=75, force_format='WEBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
