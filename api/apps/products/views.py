from django.shortcuts import render
from django.db import transaction
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from .models import Products, ProductsCategory
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from users.serializer import AuthSerializer
from users.models import User
from api.pagination import *

# Create your views here. 

class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ProductsCategory.objects.all()
    serializer_class = CategorySerializer


class ProductsListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    pagination_class = CustomPageNumber
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    """user_idの指定があればフィルターした結果を返す"""
    def get_queryset(self):
        queryset = Products.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(seller__user_id=user_id)
        return queryset

    @transaction.atomic
    def post(self, request, format=None):
        serializer = ProductsPostSerializer(data=request.data)
        print (request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProductsListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    #pagination_class = CustomUserProdPageNumber　無しとする
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    """user_idの指定があればフィルターした結果を返す"""
    def get_queryset(self):
        queryset = Products.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(seller__user_id=user_id)
        return queryset


class ProductsRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer



