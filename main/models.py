import uuid
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField(
        validators=[MinValueValidator(0, message='Price cannot be negative.')]
    )
    stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0, message='Stock cannot be negative.')]
    )
    description = models.TextField(max_length=200, null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=30)
    is_featured = models.BooleanField(default=False)
