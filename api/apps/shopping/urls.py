from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r'^orders/$', OrdersList.as_view()),
    url(r'^cart/$', CartsListCreate.as_view()),
    #path('detail/<str:pk>/', OrdersRetrieveView.as_view()),
    #url(r'^/$', AuthInfoGetView.as_view()),
    #url(r'^carts/$', CartListCreateView.as_view()),
    #url(r'^carts/update/$', CartUpdateView.as_view()),
    #url(r'^carts/delete/$', CartDeleteView.as_view()),
]