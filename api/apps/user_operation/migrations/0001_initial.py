# Generated by Django 2.2.3 on 2019-12-11 13:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20191211_2221'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='スター')),
                ('title', models.CharField(default='', help_text='レビュータイトル', max_length=30, verbose_name='レビュータイトル')),
                ('comment', models.TextField(default='', help_text='レビュー内容', verbose_name='レビュー内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='投稿時間')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.Products', verbose_name='商品')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='顧客')),
            ],
            options={
                'verbose_name': '商品レビュー',
                'verbose_name_plural': '商品レビュー',
            },
        ),
    ]
