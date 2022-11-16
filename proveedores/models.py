from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum
from configuraciones.admin import Locaciones

# Create your models here.
User = get_user_model()

class activo(Enum):
    Y = "Si"
    N = "No"

class tipos_contactos(Enum):
    P = "Principal"
    A = "Asociado"


class Proveedores(models.Model):
    proveedor = models.CharField(max_length=70)
    rfc = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    codigo_postal = models.CharField(max_length=5, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "proveedores"
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ["-proveedor"]

    def __str__(self):
        return self.proveedor


class ContactosProveedores(models.Model):
    tipo_contacto = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in tipos_contactos], default='A')
    proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='Proveedores')
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "contactos_proveedores"
        verbose_name = 'contacto proveedor'
        verbose_name_plural = 'contactos proveedores'
        ordering = ["-activo"]

    def __str__(self):
        return self.activo


class LocacionesProveedores(models.Model):
    locaciones = models.ForeignKey(Locaciones, on_delete=models.CASCADE, verbose_name='Locaciones')
    proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='Proveedores')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "locaciones_proveedores"
        verbose_name = 'locacion proveedor'
        verbose_name_plural = 'locaciones proveedores'
        ordering = ["-locaciones"]

    def __str__(self):
        return self.activo