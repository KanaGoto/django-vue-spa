from rest_framework import serializers
from .models import *
from users.serializer import *

class FavoriteSerializer(serializers.ModelSerializer):
    user = AuthSerializer()
    class Meta:
        model = Favorite
        fields = "__all__"

