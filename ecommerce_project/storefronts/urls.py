# storefronts/urls.py
from django.urls import path
from .views import StorefrontViewSet

app_name = 'storefronts'

urlpatterns = [
    path('', StorefrontViewSet.as_view({'get': 'list', 'post': 'create'}), name='storefront-list'),
    # Add more URLs specific to the storefronts app if needed
]
