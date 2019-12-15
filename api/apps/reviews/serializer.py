from rest_framework import serializers
from .models import *
from users.serializer import *

class ReviewsSerializer(serializers.ModelSerializer):
    user = AuthSerializer()
    class Meta:
        model = Reviews
        fields = "__all__"
