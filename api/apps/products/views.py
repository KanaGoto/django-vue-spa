from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Products, ProductsCategory
from .serializer import ProductsSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ProductsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ProductsCategory.objects.all()
    serializer_class = CategorySerializer


class ProductsListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    pagination_class = ProductsPagination
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    

