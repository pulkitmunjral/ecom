# In orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderedItem
from cart.serializers import CartItemSerializer

class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ['cart_item', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderedItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'users', 'items', 'total_price', 'created_at']
        read_only_fields = ['id']
