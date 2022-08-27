from django.db import models
from Cuentas.models import Cuenta
# Create your models here.
class Movimiento(models.Model):
    ID_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.FloatField()
    tipo_operacion = models.TextField()
    hora = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table="Movimientos"