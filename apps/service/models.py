from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField
import uuid


# Create your models here.
class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=255)
    details_text_editor = CKEditor5Field('Text',config_name='extends')
    cover_image = ResizedImageField(upload_to='Service/cover_image/', quality=75, force_format= 'WEBP', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
