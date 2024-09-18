import uuid
from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class ClientTestimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    client_designation = models.CharField(max_length=255)
    review = models.TextField()
    image = ResizedImageField(upload_to="ClientTestimonial/image", quality=75, force_format='WEBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
