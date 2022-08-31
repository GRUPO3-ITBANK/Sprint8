from django.db import models
# Create your models here.
class Sucursal(models.Model):
    numero_sucursal = models.IntegerField()
    nombre_sucursal = models.TextField()
    direccion_sucursal = models.CharField(max_length=150)

    class Meta:
        db_table="Sucursales"