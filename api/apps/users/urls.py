from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView, AddressListView, AddressRetrieveUpdateView

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^info/$', AuthInfoGetView.as_view()),
    url(r'^update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view()),
    url(r'^address/$', AddressListView.as_view()),
    path('address/update/<str:pk>/', AddressRetrieveUpdateView.as_view()),
]