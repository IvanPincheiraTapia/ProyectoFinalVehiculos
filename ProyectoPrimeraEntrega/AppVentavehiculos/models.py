from pyexpat import model
from django.db import models

class vehiculo(models.Model):

    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    puertas = models.IntegerField()
    usado = models.CharField(max_length=50)
    kilometros = models.IntegerField()
    año = models.IntegerField()
    precio = models.IntegerField()

class vendedor(models.Model):

    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    atencion = models.CharField(max_length=50)

class sucursales(models.Model):

    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    telefono = models.IntegerField()
