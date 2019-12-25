from django.db import models
from products.models import Products
from users.models import User
from datetime import datetime

# Create your models here.
class Cart(models.Model):
    """
    カート
    """
    user = models.ForeignKey(User, verbose_name="顧客", related_name="cart_items", on_delete=models.CASCADE)
    item = models.ForeignKey(Products, verbose_name="カート投入済み商品", related_name="cart_items", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, verbose_name="数量")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "カート"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name


class OrderDetail(models.Model):
    """
    注文履歴詳細
    """
    item = models.ForeignKey(Products, verbose_name="商品", related_name="ordered_items", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, verbose_name="数量")
    total_price = models.IntegerField(default=0, verbose_name="小計")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "注文履歴詳細"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name


class Order(models.Model):
    """
    注文履歴
    """
    user = models.ForeignKey(User, verbose_name="顧客", related_name="orders", on_delete=models.CASCADE)
    order_detail = models.ManyToManyField(OrderDetail, verbose_name="注文履歴", related_name="ordered_items")
    total_price = models.IntegerField(default=0, verbose_name="合計金額")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "注文履歴"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "注文履歴"