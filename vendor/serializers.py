from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class vendor_productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_products
        fields = '__all__'
    