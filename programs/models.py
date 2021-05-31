from django.db import models
from django.db.models.fields import TextField


class Program(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank= True)

    def __str__(self):
        return self.name
