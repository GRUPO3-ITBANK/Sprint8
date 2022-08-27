from django.db import models
from Clientes.models import Cliente
# Create your models here.
class Prestamo(models.Model):
    fecha_prestamo = models.DateTimeField(auto_now_add=True, blank=True)
    tipo = models.TextField()
    total = models.FloatField()
    ID_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table="Prestamos"