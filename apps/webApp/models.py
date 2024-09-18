import uuid
from django.db import models
from django_resized import ResizedImageField


# Create your models here.
class PricingImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_image = ResizedImageField(upload_to='pricing_images/', quality=75, force_format='WEBP')
    product_title = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length=255)
    portfolio_description = models.TextField()
    before_image = ResizedImageField(upload_to='portfolio_images/before', quality=75, force_format='WEBP')
    after_image = ResizedImageField(upload_to='portfolio_images/after', quality=75, force_format='WEBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.portfolio_title


class PortfolioExampleImage(models.Model):
    product = models.ForeignKey(Portfolio, related_name='example_images', on_delete=models.CASCADE)
    example_images = models.ImageField(upload_to='portfolio_examples/', null=True, blank=True)

    def __str__(self):
        return self.product.portfolio_title
