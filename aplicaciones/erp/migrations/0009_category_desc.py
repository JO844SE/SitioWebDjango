# Generated by Django 5.0.4 on 2024-04-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_client_product_sale_detsale_delete_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(default=2, max_length=150, unique=True, verbose_name='Descripción'),
            preserve_default=False,
        ),
    ]
