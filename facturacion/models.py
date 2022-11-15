from django.db import models
from proveedores.models import Proveedores
from solicitudes.models import Candidatos
from django.contrib.auth import get_user_model
from enum import Enum
import datetime

# Create your models here.

User = get_user_model()
#Opcciones de estatus activo.
class Activo(Enum):
    Y = "Si"
    N = "No"

class Facturas(models.Model):
    """Model que permite la creación de reportes de los candidatos que un proveedor podra facturar, 
    en el periodo de tiempo establecido"""
    
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='Proveedor')
    pre_factura_pdf = models.FileField(upload_to='prefacturas/pdf', null=True, blank=True, verbose_name='PDF Prefactura')
    pre_factura_xml = models.FileField(upload_to='prefacturas/xml',null=True,blank=True, verbose_name='XML Prefactura')
    factura_pdf = models.FileField(upload_to='facturas/pdf',null=True,blank=True, verbose_name='PDF Prefactura')
    factura_xml = models.FileField(upload_to='facturas/xml',null=True,blank=True, verbose_name='XML Prefactura')
    total_facturado = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    pagado = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table =  "facturas"
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'
        ordering = ["-created"]

    def __str__(self):
        return self.proveedores.rfc

class FacturasCandidatos(models.Model):
    """pass"""
    facturas = models.ForeignKey(Facturas, on_delete=models.CASCADE, verbose_name='Factura')
    candidatos = models.ForeignKey(Candidatos, on_delete=models.CASCADE, verbose_name='Candidato')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'facturas_candidatos'
        verbose_name = 'candidatos'
        verbose_name_plural = 'candidatos'
    
    def __str__(self):
        return self.candidatos.personas.nombre