from django.contrib import admin
from .models import Entidades, Ciudades, Locaciones, Contactos
# Register your models here.

class EntidadesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('entidad','pais','created')

class CiudadesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('ciudad','entidades','created')

class LocacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','created')
    list_display = ('locacion','locacion_name','ciudades','zona_ciudad','codigo_postal','created')

class ContactosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('contacto','telefono','email','created')

admin.site.register(Entidades, EntidadesAdmin)
admin.site.register(Ciudades, CiudadesAdmin)
admin.site.register(Locaciones, LocacionesAdmin)
admin.site.register(Contactos, ContactosAdmin)
