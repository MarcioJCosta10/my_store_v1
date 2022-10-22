from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image       = models.FileField(upload_to = 'products/')
    def __str__(self):
        return self.title
