from rest_framework import serializers
from .models import *
from users.serializer import *
from users.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductsCategory
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    seller = AuthSerializer(read_only=True)
    buyer = AuthSerializer(read_only=True)

    class Meta:    
        model =  Products
        fields = "__all__"


