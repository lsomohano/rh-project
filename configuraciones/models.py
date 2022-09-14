from django.db import models
from enum import Enum

# Create your models here.

class paises(Enum):
    mx = "México"
    us = "Estados Unidos"

class activo(Enum):
    si = "Y"
    no = "N"

class Entidades(models.Model):
    entidad = models.CharField(max_length=70)
    pais = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in paises])
    activo = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in activo])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table =  "entidades"
        verbose_name = 'entidad'
        verbose_name_plural = 'entidades'
        ordering = ["-entidad"]

    def __str__(self):
        return self.entidad

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=50)
    entidades = models.ForeignKey(Entidades, on_delete=models.CASCADE, verbose_name='Entidad')
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table =  "ciudades"
        verbose_name='ciudad'
        verbose_name_plural='ciudades'  
        ordering = ["-ciudad"]

    def __str__(self):
        return self.ciudad


class zonas_ciudades(Enum):
    cd = "Ciudad"
    apto = "Aeropuerto"


class Locaciones(models.Model):
    locacion = models.CharField(max_length=6)
    locacion_name = models.CharField(max_length=20)
    direccion = models.TextField()
    codigo_postal = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    latitud = models.CharField(max_length=15)
    longitud = models.CharField(max_length=15)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    dias_operativos = models.CharField(max_length=21)
    ciudades = models.ForeignKey(Ciudades, on_delete=models.CASCADE, verbose_name='Ciudad')
    zona_ciudad = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in zonas_ciudades], verbose_name='Zona')
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table =  "locaciones"
        verbose_name='locacion'
        verbose_name_plural='locaciones'  
        ordering = ["-locacion"]

    def __str__(self):
        return self.locacion

class Contactos(models.Model):
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    horario_inicio = models.TimeField()
    horario_termino = models.TimeField()
    dias_atencion = models.CharField(max_length=21)
    locaciones = models.ForeignKey(Locaciones, on_delete=models.CASCADE)
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table =  "contactos"
        verbose_name='contacto'
        verbose_name_plural='contactos'  
        ordering = ["-contacto"]

    def __str__(self):
        return self.contacto

