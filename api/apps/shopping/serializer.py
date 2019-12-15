from rest_framework import serializers
from .models import *
from users.serializer import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    user = AuthSerializer()
    order_detail = OrderDetailSerializer()
    class Meta:
        model = Order
        fields = "__all__"


