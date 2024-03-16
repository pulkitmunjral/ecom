from rest_framework import viewsets
from .models import Storefront
from .serializers import StorefrontSerializer


class StorefrontViewSet(viewsets.ModelViewSet):
    queryset = Storefront.objects.all()
    serializer_class = StorefrontSerializer

