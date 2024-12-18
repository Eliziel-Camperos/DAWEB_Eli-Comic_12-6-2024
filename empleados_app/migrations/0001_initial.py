# Generated by Django 5.1.3 on 2024-12-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('numero', models.IntegerField(max_length=10)),
                ('sexo', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('salario', models.FloatField()),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
    ]
