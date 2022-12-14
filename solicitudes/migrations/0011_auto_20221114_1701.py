# Generated by Django 3.2.16 on 2022-11-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0010_auto_20221104_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='cv_solicitud',
            field=models.FileField(blank=True, null=True, upload_to='candidatos/personas/cv', verbose_name='CV o Solcitud'),
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='referencias',
            field=models.FileField(blank=True, null=True, upload_to='candidatos/referencias/', verbose_name='Referencias Laborales'),
        ),
        migrations.AlterField(
            model_name='entrevistas',
            name='fecha_entrevista',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
