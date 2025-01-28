from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.URLField()
    sold = models.BooleanField()
    is_sale = models.BooleanField()
    date_of_sale = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

