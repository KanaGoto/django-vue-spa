from rest_framework import serializers
from .models import *
from users.serializer import *
from users.models import *
from products.serializer import *
from products.models import *

class FavoriteSerializer(serializers.ModelSerializer):
    item = ProductsSerializer(read_only=True)
    user = AuthSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = "__all__"

class FavoritePostSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(),write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)

    class Meta:    
        model =  Favorite
        fields = "__all__"
