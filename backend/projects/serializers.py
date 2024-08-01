from rest_framework import serializers
from .models import product

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=["id","title",'description','price',"sale_price"]