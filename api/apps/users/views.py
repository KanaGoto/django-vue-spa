from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from .serializer import UserSerializer, AddressSerializer, AuthSerializer
from .models import User, UserManager, Address

# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = AuthSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        try:
            address = AddressSerializer(Address.objects.filter(user__user_id=request.user.user_id), many=True).data
            #return Response(serializer.data)
        except Address.DoesNotExist:
            address = []

        try:
            pic = request.user.pic.url
        except:
            pic = ""

        return Response(data={
            'user_id': request.user.user_id,
            'username': request.user.username,
            'email': request.user.email,
            'profile': request.user.profile,
            'image': pic,
            'gender': request.user.gender,
            'address': address
            },
            status=status.HTTP_200_OK)


class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny,)
    serializer_class = AuthSerializer
    lookup_field = 'user_id'
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(user_id=self.request.user.user_id)
            return instance
        except User.DoesNotExist:
            raise Http404

# ユーザ削除のView(DELETE)
class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AuthSerializer
    lookup_field = 'email'
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404

class AddressListView(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Address.objects.all()
     serializer_class = AddressSerializer

class AddressRetrieveUpdateView(generics.RetrieveUpdateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Address.objects.all()
     serializer_class = AddressSerializer
     lookup_field = 'pk'

