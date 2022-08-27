# Generated by Django 4.0.6 on 2022-08-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.TextField()),
                ('total', models.FloatField()),
                ('ID_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
            ],
            options={
                'db_table': 'Prestamos',
            },
        ),
    ]