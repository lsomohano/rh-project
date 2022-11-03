from django.db import models
from enum import Enum
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class paises(Enum):
    mx = "México"
    us = "Estados Unidos"


class activo(Enum):
    Y = "Si"
    N = "No"


class Entidades(models.Model):
    entidad = models.CharField(max_length=70)
    pais = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in paises], default='mx')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in activo], default='Y')
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
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo], default='Y')
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
    ciudad = "Ciudad"
    aeropuerto = "Aeropuerto"


class Locaciones(models.Model):
    locacion = models.CharField(max_length=6)
    locacion_name = models.CharField(max_length=100)
    direccion = models.TextField()
    codigo_postal = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    latitud = models.CharField(max_length=15)
    longitud = models.CharField(max_length=15)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    dias_operativos = models.CharField(max_length=50)
    ciudades = models.ForeignKey(Ciudades, on_delete=models.CASCADE, verbose_name='Ciudad')
    zona_ciudad = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in zonas_ciudades], verbose_name='Zona',default='aeropuerto')
    indicaciones_entrevista = models.FileField(upload_to='locaciones/indicaciones/',null=True,blank=True)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in activo], default='Y')
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
    horario_inicio = models.TimeField()
    horario_termino = models.TimeField()
    dias_atencion = models.CharField(max_length=50)
    locaciones = models.ForeignKey(Locaciones, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table =  "contactos"
        verbose_name='contacto'
        verbose_name_plural='contactos'  
        ordering = ["-activo"]

    def __str__(self):
        return self.user.first_name


class PuestosNominas(models.Model):
    puesto_nomina = models.CharField(max_length=60)
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table =  "puestos_nominas"
        verbose_name='puesto'
        verbose_name_plural='puestos'  
        ordering = ["-puesto_nomina"]

    def __str__(self):
        return self.puesto_nomina


class canales_reclutamiento(Enum):
    externo = "Externo"
    interno = "Interno"

class PuestosOperativos(models.Model):
    puesto_operativo = models.CharField(max_length=60, verbose_name='Puesto')
    puestos_nominas = models.ForeignKey(PuestosNominas, on_delete=models.CASCADE)
    canal_reclutamiento = models.CharField(
        max_length=7, 
        choices=[(tag.name, tag.value) for tag in canales_reclutamiento], 
        default='externo',
        verbose_name='Reclutamiento')
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table =  "puestos_operativos"
        verbose_name='puesto operativo'
        verbose_name_plural='puestos operativos'  
        ordering = ["-puesto_operativo"]

    def __str__(self):
        return self.puesto_operativo


class LocacionesPuestos(models.Model):
    locaciones = models.ForeignKey(Locaciones, on_delete=models.CASCADE)
    puestos_operativos = models.ForeignKey(PuestosOperativos, on_delete=models.CASCADE)
    staf_requerido = models.IntegerField(null=True, blank=True, default=0)
    staf_contratado = models.IntegerField(null=True, blank=True, default=0)
    activo = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table =  "locaciones_puestos"
        verbose_name='locacione puesto'
        verbose_name_plural='locaciones puestos'  
        ordering = ["-locaciones"]

    def __str__(self):
        return self.puestos_operativos.puesto_operativo
