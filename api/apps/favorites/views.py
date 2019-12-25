from django.shortcuts import render
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.db import transaction
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

     """user_idの指定があればフィルターした結果を返す"""
     def get_queryset(self):
          queryset = Favorite.objects.all()
          user_id = self.request.query_params.get('user_id', None)
          if user_id is not None:
               queryset = queryset.filter(user__user_id=user_id)
          return queryset

     @transaction.atomic
     def post(self, request, format=None):
          serializer = FavoritePostSerializer(data=request.data)
          print (request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FavoritesDestroy(generics.DestroyAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Favorite.objects.all()
     serializer_class = FavoriteSerializer

