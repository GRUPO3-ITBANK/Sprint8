# Generated by Django 4.0.6 on 2022-09-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0009_cliente_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.CharField(choices=[('Classic', 'Classic'), ('Gold', 'Gold'), ('Black', 'Black')], max_length=100),
        ),
    ]
