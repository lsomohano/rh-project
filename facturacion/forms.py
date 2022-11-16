from django import forms
from .models import Facturas


class FacturacionForm(forms.ModelForm):
    
    class Meta:
        model = Facturas
        fields = ['proveedores','fecha_ini','fecha_fin']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control select2bs4',
            'placeholder':'Proveedor',
        })
        self.fields['fecha_ini'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha inicial',
            'data-target':'#fecha_ini'
        })
        self.fields['fecha_fin'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha final',
            'data-target':'#fecha_fin'
        })