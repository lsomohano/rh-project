from django.db import models
from django.contrib.auth import get_user_model
from configuraciones.models import Locaciones, PuestosOperativos
from enum import Enum
import datetime
# Create your models here.

User = get_user_model()

#Opcciones de estatus activo.
class Activo(Enum):
    Y = "Si"
    N = "No"

#Opciones de tipos de estatus.
class TiposEstatus(Enum):
    solicitud = "Solicitud"
    candidato = "Candidato"

#Opciones de tipos de estatus.
class Periodos(Enum):
    semanal = "Semanal"
    quincenal = "Quincenal"
    catorcenal = "Catorcenal"
    mensual = "Mensual"

#Opciones documentos.
class opciones_documentos(Enum):
    requerido = "Requerido"
    opcional = "Opcional"
    gerencial = "Gerencial"

#Opciones generos.
class Generos(Enum):
    M = "Masculino"
    F = "Femenino"
    I = "Indistinto"

#Tipos de entrevistas eventos.
class Eventos(Enum):
    entrevista = "Entrevista"
    contratacion = "Contratacion"
    ingreso = "Ingreso"

#Tipos de entrevistas eventos.
class TiposCandidatos(Enum):
    normal = "Normal"
    garantia = "Garantia"


class Estatus(models.Model):
    """Este modelo es un catologo es estatus, se podra tener estatus para las solicitudes y 
    para los candidatos"""

    estatus = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    tipos = models.CharField(max_length=9, choices=[(tag.name, tag.value) for tag in TiposEstatus], default='solicitud')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "catalogos_estatus"
        verbose_name = 'catalogo estatus'
        verbose_name_plural = 'catalogos estatus'
        ordering = ["created"]

    def __str__(self):
        return self.estatus



class SolicitudesVacantes(models.Model):
    """El sistema gestionara las solicitudes de vacantes, cada gerente podra solicitar sus vancantes 
    y el proveedor podra dar seguimiento a estas solicitudes """

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    locaciones = models.ForeignKey(Locaciones, on_delete=models.CASCADE, verbose_name='Locaciones')
    puestos_operativos = models.ForeignKey(PuestosOperativos, on_delete=models.CASCADE, verbose_name='Puestos', null=True, blank=True)
    sueldos = models.DecimalField(max_digits=20, decimal_places=2)
    comiciones = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    bono = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    garantia = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    cantidad = models.IntegerField(default=1)
    periodo_pago = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Periodos], default='quincenal')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "solicitudes_vacantes"
        verbose_name = 'solicitud vacante'
        verbose_name_plural = 'solicitudes vacantes'
        #ordering = ["-locaciones"]

    def __str__(self):
        return self.locaciones.locacion



class SolicitudesEstatus(models.Model):
    """Este modelo controla los estatus de las solicitudes, para mantener el historial de cambios de estatus
    se guarda la fecha del cambio de estus"""

    solicitudes_vacantes = models.ForeignKey(SolicitudesVacantes, on_delete=models.CASCADE, verbose_name='Solicitud')
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, verbose_name='Estatus')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "solicitudes_estatus"
        verbose_name = 'solicitud estatus'
        verbose_name_plural = 'solicitudes estatus'
        ordering = ["-created"]

    def __str__(self):
        return self.estatus.estatus



class Personas(models.Model):
    """modelo que gestiona la información personal de los candidatos"""

    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    rfc = models.CharField(max_length=20, unique=True, verbose_name='RFC')
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Generos], null=True, blank=True)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "personas"
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre



class Documentos(models.Model):
    """Este es un catoalogo de los doucnmentos que los candidatos deben presentar 
    en sus entrevistas"""
    documento = models.CharField(max_length=70, null=True, blank=True)
    descripcion = models.TextField(max_length=300, null=True, blank=True)
    consideraciones = models.CharField(max_length=9, choices=[(tag.name, tag.value) for tag in opciones_documentos], default='requerido')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "documentos"
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'
        ordering = ["created"]

    def __str__(self):
        return self.documento



class Candidatos(models.Model):
    """Este modelo gestiona los datos de los candidatos de las diferentes solicitudes"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solicitudes_vacantes = models.ForeignKey(SolicitudesVacantes, on_delete=models.CASCADE, verbose_name='Solicitudes')
    personas = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name='Personas')
    cv_solicitud = models.FileField(upload_to='candidatos/personas/cv',null=True,blank=True, verbose_name='CV o Solcitud')
    reporte_entrevista = models.FileField(upload_to='candidatos/personas/',null=True,blank=True)
    evaluacion_psicometrica = models.FileField(upload_to='candidatos/personas/',null=True,blank=True)
    referencias = models.FileField(upload_to='candidatos/referencias/',null=True,blank=True, verbose_name='Referencias Laborales')
    tipo_candidato = models.CharField(max_length=8, choices=[(tag.name, tag.value) for tag in TiposCandidatos], default='normal')
    aceptado = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "candidatos"
        verbose_name = 'candidato'
        verbose_name_plural = 'candidatos'
        ordering = ["-created"]

    def __str__(self):
        return self.personas.nombre + ' ' + self.personas.apellido_paterno + ' ' + self.personas.apellido_materno



class MotivosRechazos(models.Model):
    """Modelo que permite generar un catalogo de los motivos de rechazo"""

    motivo_rechazo = models.CharField(max_length=100)
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "motivos_rechazos"
        verbose_name = 'motivo rechazo'
        verbose_name_plural = 'motivos rechazos'

    def __str__(self):
        return self.motivo_rechazo
        

class CandidatosEstatus(models.Model):
    """Esta model gestionara los cambios de estatus de los candidatos, 
    guardando las fechas de cada cambio"""

    candidatos = models.ForeignKey(Candidatos, on_delete=models.CASCADE, verbose_name='Candidatos')
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, verbose_name='Estatus')
    motivos_rechazos = models.ForeignKey(MotivosRechazos, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Motivo de Rechazo')
    activo = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo], default='Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table =  "candidatos_estatus"
        verbose_name = 'candidato estatus'
        verbose_name_plural = 'candidatos estatus'
        ordering = ["-created"]

    def __str__(self):
        return self.estatus.estatus



class CandidatosDocumentos(models.Model):
    """Model para realizar el checklist de los documentos que el candidato presento 
    a las entrevistas"""

    candidatos = models.ForeignKey(Candidatos, on_delete=models.CASCADE, verbose_name='Candidatos')
    documentos = models.ForeignKey(Documentos, on_delete=models.CASCADE, verbose_name='Documentos')
    check_proveedor = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo],null=True,blank=True, default='N')
    check_locacion = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo],null=True,blank=True, default='N')
    
    class Meta:
        db_table =  "candidatos_documentos"
        verbose_name = 'candidato documneto'
        verbose_name_plural = 'Candidatos Documentos'

    def __str__(self):
        return self.documentos.documento

class Entrevistas(models.Model):
    """Modelo que permite gestionar las entrevistas de los candidatos"""

    candidatos = models.ForeignKey(Candidatos, on_delete=models.CASCADE, verbose_name='Candidatos')
    indicaciones = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateField()
    hora_programada = models.TimeField()
    fecha_entrevista = models.DateTimeField(null=True,blank=True)
    asistio = models.CharField(max_length=1, choices=[(tag.name, tag.value) for tag in Activo],null=True,blank=True)
    tipo_evento = models.CharField(max_length=12, choices=[(tag.name, tag.value) for tag in Eventos], default='entrevista')

    class Meta:
        db_table =  "entrevistas"
        verbose_name = 'entrevista'
        verbose_name_plural = 'entrevistas'

    def __str__(self):
        return self.tipo_evento

