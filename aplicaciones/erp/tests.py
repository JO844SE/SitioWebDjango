
'''
from SitioWeb.wsgi import *
from aplicaciones.erp.models import Type

#Listar

#Select * from tabla


#Lo que hace el ORM es que en lugar de usar
# una conculta como esta Select * from tabla  solo se manda a
# llamr el nombre del modelo con todos sus objetos



#Listar
query = Type.objects.all()
for dato in query:
    print(dato)

#Insertar

t = Type()
t.name = 'Presidente '
t.save()


#Edicion
t = Type.objects.get(pk=3)
t.name = 'Director '
t.save()



#Eliminar
t = Type.objects.get(pk=4)
t.delete()



#Listar con filtro
#Con icontains me muestra datos con mayuscula y minuscula
#con filter me muestra los datos que tengan esas cadenas que se mandadn
print("----------------- TIENEN LA LETRA A-----------------------")
t = Type.objects.filter(name__icontains='a')
for dato in t:
    print(dato)

print("----------------- TERMINAN CON R-----------------------")
#Los datos que empiezan con
t = Type.objects.filter(name__endswith='r')
for dato in t:
    print(dato)

print("---------------- CONTAR  ------------------------")
t = Type.objects.all().count()
print(t)
'''





#Models

from django.db import models
from datetime import datetime

from core.erp.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']



