from rest_framework import serializers
from .models import  Products,  ProductsCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductsCategory
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Products
        fields = "__all__"
