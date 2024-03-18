# In orders/models.py
from django.db import models

class Order(models.Model):
    user = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    items = models.ManyToManyField("cart.CartItem", through='OrderedItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.ForeignKey("cart.CartItem", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
