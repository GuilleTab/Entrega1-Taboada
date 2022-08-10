from pickle import TRUE
from django.db import models

class Articulo(models.Model):

    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    vencimiento = models.DateField(blank=True, null=TRUE)

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class Personal(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=100, null=TRUE)
    fecha_nacimiento = models.DateField(blank=TRUE, null=TRUE)
    año_ingreso = models.IntegerField()

    def __str__(self):
        return f"{self.nombre.capitalize()} - {self.apellido.upper()} - {self.puesto}"

class Vehiculos(models.Model):

    tipo_vehiculo = models.CharField(max_length=100)
    patente_vehiculo = models.CharField(max_length=20)
    estado_vehiculo = models.CharField(max_length=50)
    fecha_service = models.DateTimeField()

    def __str__(self):
        return f"{self.tipo_vehiculo} - {self.patente_vehiculo}"