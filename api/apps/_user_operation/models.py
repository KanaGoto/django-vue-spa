from django.db import models
from goods.models import Goods
from users.models import Account
from datetime import datetime
# Create your models here.

class Reviews(models.Model):
    """
    商品レビュー
    """
    prod = models.ForeignKey(Goods, verbose_name="商品", related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(Account, verbose_name="顧客", related_name="reviews", on_delete=models.CASCADE)
    star = models.IntegerField(default=1, verbose_name="スター")
    title = models.CharField(default="", max_length=30, verbose_name="レビュータイトル", help_text="レビュータイトル")
    comment = models.TextField(default="", verbose_name="レビュー内容", help_text="レビュー内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="投稿時間")

    class Meta:
        verbose_name = "商品レビュー"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
