from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_contratacion=models.DateField()
    DNI=models.TextField(max_length=25)
    
    class Meta:
        db_table="Empleados"
