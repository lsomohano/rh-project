from django.contrib import admin
from .models import Entidades, Ciudades, Locaciones, Contactos, PuestosNominas, PuestosOperativos
# Register your models here.

class EntidadesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('entidad','pais','created')


class CiudadesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('ciudad','entidades','created')


class ContactosInline(admin.StackedInline):
    model = Contactos
    readonly_fields = ('created','updated')
    #list_display = ('contacto','telefono','email','created')


class LocacionesAdmin(admin.ModelAdmin):
    inlines = [ContactosInline]
    readonly_fields = ('created','updated','created')
    list_display = ('locacion','locacion_name','ciudades','zona_ciudad','codigo_postal','created')


class PuestosOperativosInline(admin.StackedInline):
    model = PuestosOperativos


class PuestosNominasAdmin(admin.ModelAdmin):
    inlines = [PuestosOperativosInline]
    list_display = ('puesto_nomina','created')


admin.site.register(Entidades, EntidadesAdmin)
admin.site.register(Ciudades, CiudadesAdmin)
admin.site.register(Locaciones, LocacionesAdmin)
admin.site.register(PuestosNominas, PuestosNominasAdmin)
