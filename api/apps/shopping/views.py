from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from users.serializer import AuthSerializer
from users.models import User
from .models import *
from .serializer import *

# Create your views here.

class OrderSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class OrdersList(generics.ListAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     """ページング"""
     pagination_class = OrderSetPagination
     """フィルター"""
     filter_backends = (DjangoFilterBackend,)
     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
     ordering_fields = ['add_time']

class CartsListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class = CartSerializer

class CartsUpdate(generics.UpdateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class =  CartSerializer

class CartsDestroy(generics.DestroyAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class =  CartSerializer

