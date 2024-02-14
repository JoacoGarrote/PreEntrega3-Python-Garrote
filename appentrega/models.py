from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    trabajo = models.CharField(max_length=40)

class Relojes(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=20)
    
class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_de_prenda = models.DateField()
    marca = models.BooleanField()

