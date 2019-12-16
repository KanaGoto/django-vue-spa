from django.shortcuts import render
from django.db import transaction
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from .models import Products, ProductsCategory
from .serializer import ProductsSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from users.serializer import AuthSerializer
from users.models import User

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


class ProductsCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    pagination_class = ProductsPagination
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductsRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
