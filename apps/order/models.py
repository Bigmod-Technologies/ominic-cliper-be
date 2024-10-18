from django.db import models
import uuid


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField(null=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    url = models.CharField(null=True, max_length=255, blank=True)
    file_link = models.URLField(null=True)
    type = models.CharField(max_length=150)
    appointment = models.DateField()
    service = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_order = Order.objects.all().order_by('created_at').last()
            if last_order:
                last_order_number = int(last_order.order_id.split('-')[-1])
                self.order_id = f"OC-{last_order_number + 1:06d}"
            else:
                self.order_id = "OC-000001"
        super(Order, self).save(*args, **kwargs)