from django.urls import path
from .views import CartItemAPIView, CartItemDetailAPIView,CartCheckoutAPIView

urlpatterns = [
    path('cart-items/', CartItemAPIView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetailAPIView.as_view(), name='cart-item-detail'),
    path('checkout/', CartCheckoutAPIView.as_view(), name='cart-checkout'),
]