from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ReviewsCreate.as_view()),
    path('', ReviewsListViewSet)
]