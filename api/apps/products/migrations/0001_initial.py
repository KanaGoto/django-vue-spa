# Generated by Django 2.2.3 on 2019-12-08 03:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=10, verbose_name='商品識別番号')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('sold_num', models.IntegerField(default=0, verbose_name='販売数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='お気に入り登録数')),
                ('products_num', models.IntegerField(default=0, verbose_name='在庫数')),
                ('market_price', models.FloatField(default=0, verbose_name='原価')),
                ('shop_price', models.FloatField(default=0, verbose_name='販売値段')),
                ('brief', models.TextField(max_length=500, verbose_name='商品説明')),
                ('ship_free', models.BooleanField(default=True, verbose_name='送料負担')),
                ('front_image', models.ImageField(blank=True, max_length=200, null=True, upload_to=' Products/images/', verbose_name='表紙')),
                ('is_onsale', models.BooleanField(default=False, verbose_name='販売中かどうか')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='投稿時間')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='カテゴリー名', max_length=50, verbose_name='カテゴリー名')),
                ('desc', models.TextField(default='', help_text='カテゴリー説明', verbose_name='カテゴリー説明')),
                ('category_type', models.IntegerField(choices=[(1, '生鮮'), (2, '野菜'), (3, '果物'), (4, '肉'), (5, '飲料')], help_text='カテゴリータイプ', verbose_name='カテゴリータイプ')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='投稿時間')),
            ],
            options={
                'verbose_name': '商品カテゴリー',
                'verbose_name_plural': '商品カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='投稿時間')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Products', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品Images',
                'verbose_name_plural': '商品Images',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductsCategory', verbose_name='商品カテゴリー'),
        ),
    ]
