# orders/models.py
from django.db import models
from cart.models import CartItem

class Order(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
