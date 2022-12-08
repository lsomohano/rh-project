from django.contrib import admin
from .models import Estatus, Documentos, MotivosRechazos

# Register your models here.
class EstatusAdmin(admin.ModelAdmin):
    list_display = ('estatus', 'descripcion', 'tipos','activo','created')

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'activo','created')

class MotivosRechazosAdmin(admin.ModelAdmin):
    list_display = ('motivo_rechazo','tipos','activo','created','updated')


admin.site.register(Estatus, EstatusAdmin)
admin.site.register(Documentos, DocumentosAdmin)
admin.site.register(MotivosRechazos, MotivosRechazosAdmin)