# Generated by Django 3.2.15 on 2022-09-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0002_auto_20220921_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudades',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=5),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=5),
        ),
        migrations.AlterField(
            model_name='entidades',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=20),
        ),
        migrations.AlterField(
            model_name='locaciones',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=1),
        ),
        migrations.AlterField(
            model_name='locaciones',
            name='zona_ciudad',
            field=models.CharField(choices=[('ciudad', 'Ciudad'), ('aeropuerto', 'Aeropuerto')], default='aeropuerto', max_length=10, verbose_name='Zona'),
        ),
        migrations.AlterField(
            model_name='locacionespuestos',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=5),
        ),
        migrations.AlterField(
            model_name='puestosnominas',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=5),
        ),
        migrations.AlterField(
            model_name='puestosoperativos',
            name='activo',
            field=models.CharField(choices=[('Y', 'Si'), ('N', 'No')], default='Y', max_length=5),
        ),
    ]