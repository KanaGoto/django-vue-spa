from django.db import models
from products.models import Products
from users.models import User
from datetime import datetime
# Create your models here.

class Favorite(models.Model):
    """
    お気に入り商品
    """
    item = models.ForeignKey(Products, verbose_name="商品", related_name="favorites", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, verbose_name="顧客", related_name="favorites", on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "お気に入り商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name