from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'$', ReviewsListCreate.as_view()),
    path('update/<str:pk>/', ReviewsRetrieveUpdate.as_view()),
   #url(r'^create/$', ReviewsCreate.as_view()),
 ]