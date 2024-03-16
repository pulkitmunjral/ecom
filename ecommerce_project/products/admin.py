from django.contrib import admin
from .models import Color,Size,Category,Product
# Register your models here.

admin.register(Product)
admin.register(Color)
admin.register(Size)
admin.register(Category)