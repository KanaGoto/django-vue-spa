from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import User, UserManager, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'profile',
            'is_active',
            'is_staff',
            'is_admin',
            'pic',
            'gender',
            'date_joined',
            'address', #モデルには存在しない追加する新フィールド
        ]

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance

    def get_address(self, obj):
        try:
            address_abstruct_contents = AddressSerializer(Address.objects.all().filter(user = User.objects.get(user_id=obj.user_id)), many=True).data
            #↑ここを"address.objects.all().filter(target_article = Article.objects.get(id=obj.id)"
            #とだけにすると、"Item is not JSON serializable"というエラーが出ますので
            #Serializer(出力させたいもの).data　という処理が必要です。
            return address_abstruct_contents
        except:
            address_abstruct_contents = None
            return address_abstruct_contents


