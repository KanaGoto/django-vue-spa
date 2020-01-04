from django.db import models
from products.models import *
from users.models import *
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
    PAYMENT_CHOICES = (("0", "代引き"), ("1", "PayPay"), ("2", "LinePay"), ("3", "VISA"))
    DELIVERYTIME_CHOICES = (("0", "最短"), ("1", "午前中"), ("2", "12:00 ~ 14:00"), ("3", "14:00 ~ 17:00"), ("4", "17:00 ~ 19:00"))

    user = models.ForeignKey(User, verbose_name="顧客", related_name="orders", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name="お届け先", related_name="orders", on_delete=models.CASCADE)
    order_detail = models.ManyToManyField(OrderDetail, verbose_name="注文履歴", related_name="ordered_items")
    payment = models.CharField(choices = PAYMENT_CHOICES,default="0", max_length=1, verbose_name="支払い方法")
    delivery_date = models.TextField(default="", verbose_name="お届け日")
    delivery_time = models.CharField(choices = DELIVERYTIME_CHOICES, default="0", max_length=1, verbose_name="お届け時間帯")
    total_price = models.CharField(default=0, max_length=10, verbose_name="合計金額")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "注文履歴"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "注文履歴"