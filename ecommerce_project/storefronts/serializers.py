from rest_framework import serializers
from .models import Storefront

class StorefrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storefront
        fields = '__all__'