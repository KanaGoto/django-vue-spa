from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .serializer import *
from .models import * 
# Create your views here.

class FavoriteSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class FavoritesListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Favorite.objects.all()
     serializer_class = FavoriteSerializer
     """ページング"""
     pagination_class = FavoriteSetPagination

class FavoritesDestroy(generics.DestroyAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Favorite.objects.all()
     serializer_class = FavoriteSerializer

