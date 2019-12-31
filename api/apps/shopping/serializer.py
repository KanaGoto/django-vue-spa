from rest_framework import serializers
from .models import *
from users.serializer import *
from users.models import *
from products.serializer import *
from products.models import *

class CartSerializer(serializers.ModelSerializer):
    item = ProductsSerializer(read_only=True)
    user = AuthSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"

class CartPostSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(),write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Cart
        fields = "__all__"

class OrderDetailSerializer(serializers.ModelSerializer):
    item = ProductsSerializer(read_only=True)
    class Meta:
        model = OrderDetail
        fields = "__all__"

class OrderDetailPostSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(),write_only=True)
    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True,read_only=True)
    user = AuthSerializer(read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

class OrderPostSerializer(serializers.ModelSerializer):
    order_detail = serializers.PrimaryKeyRelatedField(queryset=OrderDetail.objects.all(),write_only=True,many=True,)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Order
        fields = "__all__"