from django.db import models
from django.conf import settings

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140)
    apellidos = models.CharField(max_length=140)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=140)
    carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alumno_alumno'


class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alumno_carrera'

# Create your models here.
