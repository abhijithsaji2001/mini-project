from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    address = models.TextField(null=True)