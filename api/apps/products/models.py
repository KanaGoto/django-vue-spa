from datetime import datetime
from django.db import models
from users.models import User

class ProductsCategory(models.Model):
    """
    商品カテゴリー
    """
    name = models.CharField(default="", max_length=50, verbose_name="カテゴリー名", help_text="カテゴリー名")
    desc = models.TextField(default="", verbose_name="カテゴリー説明", help_text="カテゴリー説明")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="投稿時間")

    class Meta:
        verbose_name = "商品カテゴリー"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

def get_or_create_buyer():
    buyer, _ = User.objects.get_or_create(username="unknown", email="xxx@sample.com", password="zaq12wsx")
    return buyer

class Products(models.Model):
    
    """
    商品
    """
    name = models.CharField(max_length=100, verbose_name="商品名")
    category = models.ForeignKey(ProductsCategory, null=True,blank=True, verbose_name="商品カテゴリー", related_name="products", on_delete=models.CASCADE)
    sold_num = models.IntegerField(default=0, verbose_name="販売数")
    fav_num = models.IntegerField(default=0, verbose_name="お気に入り登録数")
    products_num = models.IntegerField(default=0, verbose_name="在庫数")
    market_price = models.FloatField(default=0, verbose_name="原価")
    shop_price = models.FloatField(default=0, verbose_name="販売値段")
    brief = models.TextField(max_length=500, verbose_name="商品説明")
    ship_free = models.BooleanField(default=True, verbose_name="送料負担")
    image = models.ImageField(max_length=200, upload_to=" products/images/",
                                          null=True, blank=True, verbose_name="画像")
    is_onsale = models.BooleanField(default=True, verbose_name="販売中")
    seller = models.ForeignKey(User,null=True, verbose_name="販売者", related_name="products_sold", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, null=True, verbose_name="購入者", related_name="products_purchased", on_delete=models.SET_NULL, default=get_or_create_buyer,)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="投稿時間")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.buyer is None:
            self.buyer = User.get_default_params()
        super(Products, self).save(*args, **kwargs)


class  ProductsImage(models.Model):
    """
    商品Images
    """
    products = models.ForeignKey(Products, verbose_name="商品", related_name="images", null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="", verbose_name="画像", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="投稿時間")

    class Meta:
        verbose_name = "商品Images"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product.name

