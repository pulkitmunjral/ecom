from django.urls import path
from .views import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    path('', CustomerAPIView.as_view(), name='users-list'),
    path('<int:pk>/', CustomerDetailAPIView.as_view(), name='users-detail'),
]
