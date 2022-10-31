from django.contrib import admin
from .models import Estatus, Documentos

# Register your models here.
class EstatusAdmin(admin.ModelAdmin):
    list_display = ('estatus', 'descripcion', 'tipos','activo','created')

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'activo','created')

admin.site.register(Estatus, EstatusAdmin)
admin.site.register(Documentos, DocumentosAdmin)