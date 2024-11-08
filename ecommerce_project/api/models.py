# api/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(1)])
    category = models.CharField(max_length=50)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=20, unique=True)
    shipping_address = models.TextField()
