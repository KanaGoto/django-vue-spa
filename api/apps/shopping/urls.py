from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r'^orders/$', OrdersListCreate.as_view()),
    url(r'^orders/detail/$', OrdersDetailListCreate.as_view()),
    url(r'^cart/$', CartsListCreate.as_view()),
    path('cart/update/<str:pk>/', CartsUpdate.as_view()),
    path('cart/delete/<str:pk>/', CartsDestroy.as_view()),    
]