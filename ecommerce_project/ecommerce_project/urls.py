# ecommerce_project/urls.py
from django.urls import path, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Your API Documentation')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('client/', include('clients.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('products/', include('products.urls')),
    path('storefronts/', include('storefronts.urls')),
    path('users/', include('users.urls')),
    path('docs/', schema_view),
]