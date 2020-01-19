from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, permissions
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.db import transaction
from users.serializer import *
from users.models import *
from .models import *
from .serializer import *
from api.pagination import *

# Create your views here.

class OrdersDetailListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = OrderDetail.objects.all()
     serializer_class = OrderDetailSerializer
     
     @transaction.atomic
     def post(self, request, format=None):
          serializer = OrderDetailPostSerializer(data=request.data)
          print (request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Order.objects.order_by('add_time')
     serializer_class = OrderSerializer
     """ページング"""
     pagination_class = CustomUserProdPageNumber
     """フィルター"""
     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
     ordering_fields = ['id']
     ordering = ['id']

     """user_idの指定があればフィルターした結果を返す"""
     def get_queryset(self):
          queryset = Order.objects.all()
          user_id = self.request.query_params.get('user_id', None)
          if user_id is not None:
               queryset = queryset.filter(user__user_id=user_id)
          return queryset
     
     @transaction.atomic
     def post(self, request, format=None):
          serializer = OrderPostSerializer(data=request.data)
          print (request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartsListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class = CartSerializer

     """user_idの指定があればフィルターした結果を返す"""
     def get_queryset(self):
          queryset = Cart.objects.all()
          user_id = self.request.query_params.get('user_id', None)
          if user_id is not None:
               queryset = queryset.filter(user__user_id=user_id)
          return queryset

     @transaction.atomic
     def post(self, request, format=None):
          serializer = CartPostSerializer(data=request.data)
          print (request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartsUpdate(generics.UpdateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class =  CartSerializer

class CartsDestroy(generics.DestroyAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Cart.objects.all()
     serializer_class =  CartSerializer

