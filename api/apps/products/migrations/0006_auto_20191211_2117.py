# Generated by Django 2.2.3 on 2019-12-11 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscategory',
            name='category_type',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.ProductsCategory', verbose_name='商品カテゴリー'),
        ),
    ]