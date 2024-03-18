from rest_framework import generics, status
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from orders.models import Order, OrderedItem
from orders.serializers import OrderSerializer


class CartItemAPIView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartCheckoutAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(cart__user=user)

        # Calculate total price
        total_price = sum(item.total_price for item in cart_items)

        # Create order
        order = Order.objects.create(user=user, total_price=total_price)

        # Move cart items to ordered items
        for cart_item in cart_items:
            OrderedItem.objects.create(order=order, cart_item=cart_item, quantity=cart_item.quantity, unit_price=cart_item.product.price)
            cart_item.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)