from django.contrib import admin
from .models import Estatus
# Register your models here.
class EstatusAdmin(admin.ModelAdmin):
    list_display = ('estatus', 'descripcion', 'tipos','activo','created')


admin.site.register(Estatus, EstatusAdmin)