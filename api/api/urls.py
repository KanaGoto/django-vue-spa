"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path, re_path, include
from django.views.static import serve
from api.settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token 
from django.conf.urls import url
from django.contrib.auth import views as auth_views#追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^login/', obtain_jwt_token),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^users/', include('users.urls')),
    re_path(r'^products/', include('products.urls')),
    re_path(r'^shopping/', include('shopping.urls')),
    re_path(r'^reviews/', include('reviews.urls')),
    re_path(r'^favorites/', include('favorites.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]