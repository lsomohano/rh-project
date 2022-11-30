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

class FacturacionPrefacturaForm(forms.ModelForm):
    
    class Meta:
        model = Facturas
        fields = ['fecha_ini','fecha_fin','proveedores','pre_factura_pdf','pre_factura_xml']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control select2bs4 ',
            'placeholder':'Proveedor',
            'readonly':"readonly"
        })
        self.fields['fecha_ini'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha inicial',
            'data-target':'#fecha_ini',
            'readonly':"readonly"
        })
        self.fields['fecha_fin'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha final',
            'data-target':'#fecha_fin',
            'readonly':"readonly"
        })
        self.fields['pre_factura_pdf'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Pre Factura PDF',
        })
        self.fields['pre_factura_xml'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Pre Factura XML',
        })

class FacturacionfacturaForm(forms.ModelForm):
    
    class Meta:
        model = Facturas
        fields = ['fecha_ini','fecha_fin','proveedores','factura_pdf','factura_xml','total_facturado']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control select2bs4 ',
            'placeholder':'Proveedor',
            'readonly':"readonly"
        })
        self.fields['fecha_ini'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha inicial',
            'data-target':'#fecha_ini',
            'readonly':"readonly"
        })
        self.fields['fecha_fin'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha final',
            'data-target':'#fecha_fin',
            'readonly':"readonly"
        })
        self.fields['factura_pdf'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Factura PDF',
        })
        self.fields['factura_xml'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Factura XML',
        })
        self.fields['total_facturado'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Total Faturado',
        })
        