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
from django.urls import path, re_path, include
from django.views.static import serve
from api.settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
import xadmin
from goods.views import GoodsListViewSet
from goods.views import CategoryViewSet
from user_operation.views import ReviewsViewSet
from rest_framework_jwt.views import obtain_jwt_token # 追加
from django.conf.urls import url

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewSet, base_name="categorys")
router.register(r'reviews', ReviewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^login/', obtain_jwt_token),
    re_path(r'^users/', include('users.urls')),
    #path('auth/', obtain_jwt_token), # 追加
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path('^', include(router.urls)),
]