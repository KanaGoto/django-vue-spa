# Generated by Django 2.2.3 on 2019-12-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191208_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductsCategory', verbose_name='商品カテゴリー'),
        ),
        migrations.AlterField(
            model_name='productsimage',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='products.Products', verbose_name='商品'),
        ),
    ]