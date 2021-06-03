import uuid

from django.db import models

from django_countries.fields import CountryField


class Order(models.Model):
    order_number = models.CharField(max_length=16, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(null=False, blank=False)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=30, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    status = models.CharField(max_length=50, null=False, blank=False, default='not_paid')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number