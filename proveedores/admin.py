from django.contrib import admin
from .models import Proveedores, ContactosProveedores, LocacionesProveedores

# Register your models here.

class ContactosProveedoresInline(admin.StackedInline):
    model = ContactosProveedores

class LocacionesProveedoresInline(admin.StackedInline):
    model = LocacionesProveedores

class ProveedoresAdmin(admin.ModelAdmin):
    inlines = [ContactosProveedoresInline,LocacionesProveedoresInline]
    list_display = ('proveedor', 'rfc', 'razon_social','created')


admin.site.register(Proveedores, ProveedoresAdmin)