# In users/urls.py
from django.urls import path
from .views import UserAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='users-detail'),
]
