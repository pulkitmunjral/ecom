# ecommerce_project/urls.py
from django.urls import path, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Your API Documentation')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('storefronts/', include('storefronts.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('docs/', schema_view),
]