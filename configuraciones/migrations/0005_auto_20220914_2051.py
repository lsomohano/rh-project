# Generated by Django 3.2.15 on 2022-09-14 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0004_auto_20220914_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudades',
            old_name='entidades_id',
            new_name='entidades',
        ),
        migrations.RenameField(
            model_name='contactos',
            old_name='locaciones_id',
            new_name='locaciones',
        ),
        migrations.RenameField(
            model_name='locaciones',
            old_name='ciudades_id',
            new_name='ciudades',
        ),
    ]
