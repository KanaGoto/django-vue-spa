# Generated by Django 2.2.3 on 2020-01-03 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='数量')),
                ('total_price', models.IntegerField(default=0, verbose_name='小計')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='products.Products', verbose_name='商品')),
            ],
            options={
                'verbose_name': '注文履歴詳細',
                'verbose_name_plural': '注文履歴詳細',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(choices=[('0', '代引き'), ('1', 'PayPay'), ('2', 'LinePay'), ('3', 'VISA')], default='0', max_length=1, verbose_name='支払い方法')),
                ('delivery_date', models.TextField(default='', verbose_name='お届け日')),
                ('delivery_time', models.CharField(choices=[('0', '最短'), ('1', '午前中'), ('2', '12:00 ~ 14:00'), ('3', '14:00 ~ 17:00'), ('4', '17:00 ~ 19:00')], default='0', max_length=1, verbose_name='お届け時間帯')),
                ('total_price', models.CharField(default=0, max_length=10, verbose_name='合計金額')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('order_detail', models.ManyToManyField(related_name='ordered_items', to='shopping.OrderDetail', verbose_name='注文履歴')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='顧客')),
            ],
            options={
                'verbose_name': '注文履歴',
                'verbose_name_plural': '注文履歴',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='数量')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='products.Products', verbose_name='カート投入済み商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to=settings.AUTH_USER_MODEL, verbose_name='顧客')),
            ],
            options={
                'verbose_name': 'カート',
                'verbose_name_plural': 'カート',
            },
        ),
    ]
