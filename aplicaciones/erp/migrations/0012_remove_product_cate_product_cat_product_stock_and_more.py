# Generated by Django 5.0.4 on 2024-04-17 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_alter_category_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cate',
        ),
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.category', verbose_name='Categoría'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta'),
        ),
    ]
