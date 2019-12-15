from rest_framework import serializers
from .models import  Products,  ProductsCategory
from users.serializer import AuthSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductsCategory
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = AuthSerializer()
    buyer = AuthSerializer()

    class Meta:    
        model =  Products
        fields = "__all__"


