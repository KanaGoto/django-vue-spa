from django.conf.urls import include, url
from rest_framework import routers
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$', ProductsListCreateView.as_view()), 
    path('users/', UserProductsListView.as_view()),
    path('retrieve/<str:pk>/', ProductsRetrieveUpdateView.as_view()),
    url(r'^category/$', CategoryListCreateView.as_view()),
 ]