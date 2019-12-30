from django.contrib import admin
from .models import *
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user", "item", "amount", "add_time"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "_order_detail","total_price", "add_time"]
    
    def _order_detail(self, row):
        return ','.join([x.item.name for x in row.order_detail.all()])

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["amount", "item", "total_price", "add_time"]


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
