from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .models import Goods
from .serializer import GoodsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import GoodsFilter
from .models import GoodsCategory
from .serializer import CategorySerializer
# Create your views here.

class GoodsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     queryset = Goods.objects.all()
     serializer_class = GoodsSerializer
     """ページング"""
     pagination_class = GoodsSetPagination
     """フィルター"""
     filter_backends = (DjangoFilterBackend,)
     #filterset_fields = ('name', 'shop_price')
     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
     filterset_class = GoodsFilter
     search_fields = ['name', 'goods_brief']
     ordering_fields = ['shop_price']

class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


    

