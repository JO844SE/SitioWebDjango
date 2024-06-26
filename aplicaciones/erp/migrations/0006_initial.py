# Generated by Django 5.0.4 on 2024-04-11 17:47

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp', '0005_remove_employee_cated_remove_employee_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'tipo_empleado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('nit', models.CharField(max_length=10, unique=True, verbose_name='Nit')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')),
                ('date_updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Edad')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Salario')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('gender', models.CharField(max_length=50, verbose_name='Sexo')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d', verbose_name='Imagen')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d', verbose_name='Cvitae')),
                ('cated', models.ManyToManyField(to='erp.category', verbose_name='Categoria')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.type', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
