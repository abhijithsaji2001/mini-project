from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    CART_STAGE = "CART"
    ORDERED_STAGE = "ORDERED"
    STATUS_CHOICES = [
        (CART_STAGE, "Cart"),
        (ORDERED_STAGE, "Ordered"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CART_STAGE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.TextField()
