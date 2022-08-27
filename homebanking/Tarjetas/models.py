from django.db import models
from Clientes.models import Cliente
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Tarjeta(models.Model):
    numero = models.CharField(max_length=20)
    cvv = models.PositiveIntegerField(validators=[MinValueValidator(100),MaxValueValidator(999)])
    fecha_otorgamiento = models.DateField()
    fecha_vencimiento = models.DateField()
    tipo = models.CharField(max_length=25)
    marca = models.CharField(max_length=50)
    ID_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)