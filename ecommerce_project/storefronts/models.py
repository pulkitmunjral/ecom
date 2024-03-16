from django.db import models

class Storefront(models.Model):
    company = models.ForeignKey("clients.Company", on_delete=models.CASCADE, related_name='storefronts')
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
