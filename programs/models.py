from django.db import models


class Program(models.Model):
    sku = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50)
    insight = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField()
    day_one = models.CharField(max_length=500, null=True, blank=False)
    day_two = models.CharField(max_length=500, null=True, blank=False)
    day_three = models.CharField(max_length=500, null=True, blank=False)
    day_four = models.CharField(max_length=500, null=True, blank=False)
    day_five = models.CharField(max_length=500, null=True, blank=False)
    day_six = models.CharField(max_length=500, null=True, blank=False)
    day_seven = models.CharField(max_length=500, null=True, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank= False)

    def __str__(self):
        return self.name
