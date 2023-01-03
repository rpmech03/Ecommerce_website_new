from django.db import models
from app.models import Product

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10, unique=True)
    alternate_mobile_number = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50, unique=True)
    business_name = models.CharField(max_length=200, unique=True)
    shop_image = models.ImageField(upload_to ="shop_images")
    password = models.CharField(max_length=200)
    shop_documents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default= True)

    def __str__(self) -> str:
        return self.name

class vendor_products(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.product.title + " " + self.vendor.name    
