from django.db import models
from Clientes.models import Cliente
# Create your models here.
class Cuenta(models.Model):
    ID_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance=models.FloatField()
    iban=models.TextField()
    tipo_cuenta=models.CharField(max_length=20)

    class Meta:
        db_table="Cuentas"
