# Generated by Django 2.2.3 on 2019-12-03 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='商品識別番号')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('click_num', models.IntegerField(default=0, verbose_name='クリック数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='販売数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='お気に入り登録数')),
                ('goods_num', models.IntegerField(default=0, verbose_name='在庫数')),
                ('market_price', models.FloatField(default=0, verbose_name='原価')),
                ('shop_price', models.FloatField(default=0, verbose_name='販売値段')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='商品説明')),
                ('ship_free', models.BooleanField(default=True, verbose_name='送料負担')),
                ('goods_front_image', models.ImageField(blank=True, max_length=200, null=True, upload_to='goods/images/', verbose_name='表紙')),
                ('is_new', models.BooleanField(default=False, verbose_name='新品なのか')),
                ('is_hot', models.BooleanField(default=False, verbose_name='売れているのか')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='カテゴリー名', max_length=50, verbose_name='カテゴリー名')),
                ('code', models.CharField(default='', help_text='カテゴリーコード', max_length=30, verbose_name='カテゴリーコード')),
                ('desc', models.TextField(default='', help_text='カテゴリー説明', verbose_name='カテゴリー説明')),
                ('category_type', models.IntegerField(choices=[(1, '一級カテゴリー'), (2, '二級カテゴリー'), (3, '三級カテゴリー')], help_text='カテゴリーレベル', verbose_name='カテゴリーレベル')),
                ('is_tab', models.BooleanField(default=False, help_text='ナビなのか', verbose_name='ナビなのか')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
                ('parent_category', models.ForeignKey(blank=True, help_text='親カテゴリー', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='親カテゴリー')),
            ],
            options={
                'verbose_name': '商品カテゴリー',
                'verbose_name_plural': '商品カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='人気キーワード')),
                ('index', models.IntegerField(default=0, verbose_name='並び順')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
            ],
            options={
                'verbose_name': '人気キーワード',
                'verbose_name_plural': '人気キーワード',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品カテゴリー')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods')),
            ],
            options={
                'verbose_name': 'ホームページ商品カテゴリー広告',
                'verbose_name_plural': 'ホームページ商品カテゴリー広告',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品swiperImages',
                'verbose_name_plural': '商品swiperImages',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='ブランド名', max_length=30, verbose_name='ブランド名')),
                ('desc', models.CharField(default='', help_text='ブランド説明', max_length=200, verbose_name='ブランド説明')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品カテゴリー名')),
            ],
            options={
                'verbose_name': 'ブランド',
                'verbose_name_plural': 'ブランド',
                'db_table': 'goods_goodsbrand',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品カテゴリー'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='ホームページswiper用画像')),
                ('index', models.IntegerField(default=0, verbose_name='swiper順番')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='挿入時間')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'swiper用の商品image',
                'verbose_name_plural': 'swiper用の商品image',
            },
        ),
    ]
