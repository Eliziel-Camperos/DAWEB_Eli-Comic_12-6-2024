# Generated by Django 5.1.3 on 2024-12-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id_devo', models.IntegerField(primary_key=True, serialize=False)),
                ('id_venta', models.IntegerField()),
                ('id_comic', models.IntegerField()),
                ('fecha_devo', models.DateField()),
                ('motivo', models.CharField(max_length=250)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
