# Generated by Django 3.2.16 on 2022-11-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20221011_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactosproveedores',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='locacionesproveedores',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
