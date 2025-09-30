from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=42)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    actual_price = models.IntegerField()
    image = models.ImageField(upload_to="media/products")
    seller = models.CharField(max_length=50, default='Unknown')

    DRESS = 'dress'
    COSSMETICS = 'cosmetics'
    GROCERY = 'grocery'
    SHOES = 'shoes'
    WATCHES = 'watches'

    PRODUCT_TYPES = [
        (DRESS, "dress"),
        (COSSMETICS, "cosmetics"),
        (GROCERY, "grocery"),
        (SHOES, "shoes"),
        (WATCHES, "watches")
    ]
    product_type = models.CharField(choices=PRODUCT_TYPES, default=None, max_length=100)

    def __str__(self):
        return self.title
