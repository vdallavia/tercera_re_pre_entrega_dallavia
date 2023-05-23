from django.db import models

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=64)

class Turnos(models.Model):
    fecha_hora = models.DateTimeField()
    servicio = models.CharField(max_length=64)
    staff = models.CharField(max_length=64)

class Staff(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    especialidad = models.CharField(max_length=64)

class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    DNI = models.CharField(max_length=32)