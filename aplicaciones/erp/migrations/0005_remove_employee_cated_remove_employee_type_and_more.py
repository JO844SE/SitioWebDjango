# Generated by Django 5.0.4 on 2024-04-11 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_category_alter_type_name_employee_cated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='cated',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='type',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
