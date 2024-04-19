

from SitioWeb.settings import MEDIA_URL, STATIC_URL
from django.forms import model_to_dict
'''
from django.db import models
from datetime import datetime

#Entidad tipo de empleado
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        #Agrego este atributo para que en la base de datos se muestre la tabla con el nombre empleado
        db_table = "tipo_empleado"
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        #Agrego este atributo para que en la base de datos se muestre la tabla con el nombre empleado
        db_table = "categoria"
        ordering = ['id']


#Entidad empleado
class Employee(models.Model):
    #Permite crear una tabla de detalle de la relacionde categoria y empleado
    cated = models.ManyToManyField(Category, verbose_name="Categoria")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Tipo")
    names = models.CharField(max_length=150, verbose_name="Nombres")
    nit = models.CharField(max_length=10, unique=True, verbose_name="Nit")
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")
    age = models.PositiveIntegerField(default=0, verbose_name="Edad")
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Salario")
    state = models.BooleanField(default=True, verbose_name="Estado")
    gender = models.CharField(max_length=50, verbose_name="Sexo")
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True, verbose_name="Imagen")
    cvitae = models.FileField(upload_to="cvitae/%Y/%m/%d", null=True, blank=True, verbose_name="Cvitae")

#Es un metos que representra a la entidad Employee
    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        #Agrego este atributo para que en la base de datos se muestre la tabla con el nombre empleado
        db_table = "empleado"
        ordering = ['id']
        '''


#Modelos

from django.db import models
from datetime import datetime

from aplicaciones.erp.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=150, unique=True, verbose_name='Descripción', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = "categoria"
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name

    # def toJSON(self):
    #     item = model_to_dict(self)
    #     item['full_name'] = '{} / {}'.format(self.name, self.cat.name)
    #     item['cat'] = self.cat.toJSON()
    #     item['image'] = self.get_image()
    #     item['pvp'] = format(self.pvp, '.2f')
    #     return item

#Método
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = "producto"
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
        db_table = "cliente"
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
        db_table = "venta"
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
        db_table = "DetalleVenta"
        ordering = ['id']










