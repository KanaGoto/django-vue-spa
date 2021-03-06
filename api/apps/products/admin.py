from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from .models import Products, ProductsImage, ProductsCategory


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image", "sold_num","fav_num", "products_num", "market_price",
                    "shop_price", "brief","is_onsale", "add_time"]
    search_fields = ['name']
    list_editable = ["is_onsale"]
    list_filter = ["name", "sold_num","fav_num", "products_num", "market_price",
                   "shop_price", "is_onsale", "add_time"]


class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "add_time"]
    list_filter = ["name"]
    search_fields = ['name']


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsCategory, ProductsCategoryAdmin)
