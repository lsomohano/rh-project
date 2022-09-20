from django.contrib import admin
from .models import Proveedores, ContactosProveedores

# Register your models here.

class ContactosProveedoresInline(admin.StackedInline):
    model = ContactosProveedores


class ProveedoresAdmin(admin.ModelAdmin):
    inlines = [ContactosProveedoresInline]
    list_display = ('proveedor', 'rfc', 'razon_social','created')


admin.site.register(Proveedores, ProveedoresAdmin)