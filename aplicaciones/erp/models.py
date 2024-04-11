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
    name = models.CharField(max_length=150, verbose_name="Nombre")

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


#ORM  Mapeo de objetos relacionales






