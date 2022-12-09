from django.contrib import admin
from .models import Estatus, Documentos, MotivosRechazos, SolicitudesVacantes, Candidatos, Personas

# Register your models here.
class EstatusAdmin(admin.ModelAdmin):
    list_display = ('estatus', 'descripcion', 'tipos','activo','created')

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'activo','created')

class MotivosRechazosAdmin(admin.ModelAdmin):
    list_display = ('motivo_rechazo','tipos','activo','created','updated')

class CandidatosInline(admin.StackedInline):
    model = Candidatos
    list_display = ('personas','created')

class SolicitudesVacantesAdmin(admin.ModelAdmin):
    model = SolicitudesVacantes
    inlines = [CandidatosInline]
    readonly_fields = ('user','created','updated')
    list_display = ('puestos_operativos','locaciones','cantidad','created')

admin.site.register(SolicitudesVacantes, SolicitudesVacantesAdmin)
admin.site.register(Estatus, EstatusAdmin)
admin.site.register(Documentos, DocumentosAdmin)
admin.site.register(MotivosRechazos, MotivosRechazosAdmin)
