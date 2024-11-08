from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid

# Model for the products  
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(1)])
    category = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)  
    def __str__(self):
        return self.name


# Model for the Cart Items
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    class Meta:
        unique_together = ('user', 'product')  


# Model for the Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4) 
    shipping_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


