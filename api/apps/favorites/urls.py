from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', FavoritesListCreate.as_view()),
    path('delete/<str:pk>/', FavoritesDestroy.as_view()),
    #url(r'^create/$', ReviewsCreate.as_view()),

 ]