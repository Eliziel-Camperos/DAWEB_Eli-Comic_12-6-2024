# Generated by Django 5.1.3 on 2024-12-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('id_venta', models.IntegerField()),
                ('fecha_fac', models.DateField()),
                ('total', models.FloatField()),
                ('metodo_pago', models.CharField(max_length=50)),
                ('id_cliente', models.IntegerField()),
                ('descuento', models.IntegerField()),
            ],
        ),
    ]