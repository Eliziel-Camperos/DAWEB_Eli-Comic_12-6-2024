# Generated by Django 5.1.3 on 2024-12-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devoluciones_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='fecha_devo',
            field=models.CharField(max_length=50),
        ),
    ]