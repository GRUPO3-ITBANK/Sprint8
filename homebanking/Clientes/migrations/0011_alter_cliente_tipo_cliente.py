# Generated by Django 4.0.6 on 2022-09-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0010_alter_cliente_tipo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.CharField(max_length=100),
        ),
    ]
