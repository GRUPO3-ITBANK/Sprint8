from django.db import models
class Cliente(models.Model):
    
    email = models.EmailField(verbose_name='mail address',max_length=255)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    DNI=models.CharField(max_length=50,unique=True,)
    fecha_de_nac=models.DateField()
    TIPOS=(
        ('C','Classic'),
        ('G','Gold'),
        ('B','Black')
    )
    tipo_cliente = models.CharField(max_length=1,choices=TIPOS)
    
    def __str__(self):
        return  " (ID: " + str(self.id) + "): "+ self.nombre +" "+  self.apellido +", DNI: " + self.DNI 

    class Meta:
        db_table = 'Clientes'




