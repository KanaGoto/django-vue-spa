from rest_framework import serializers
from .models import *
from users.serializer import *
from users.models import *
from products.serializer import *
from products.models import *

class ReviewsSerializer(serializers.ModelSerializer):
    prod = ProductsSerializer(read_only=True)
    user = AuthSerializer(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"

class ReviewsPostSerializer(serializers.ModelSerializer):
    prod = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(),write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"