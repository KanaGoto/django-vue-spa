from django.shortcuts import render
from rest_framework import mixins, viewsets, generics, permissions
from .serializer import ReviewsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from .filters import ReviewsFilter
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from .models import Reviews

# Create your views here.

class ReviewsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ReviewsListCreate(generics.ListCreateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Reviews.objects.all()
     serializer_class = ReviewsSerializer
     """ページング"""
     pagination_class = ReviewsSetPagination
     """フィルター"""
     filter_backends = (DjangoFilterBackend,)
     #filterset_fields = ('name', 'shop_price')
     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
     filterset_class = ReviewsFilter
     search_fields = ['star']
     ordering_fields = ['add_time', 'star']

class ReviewsRetrieveUpdate(generics.RetrieveUpdateAPIView):
     permission_classes = (permissions.AllowAny,)
     queryset = Reviews.objects.all()
     serializer_class = ReviewsSerializer
     lookup_field = 'pk'