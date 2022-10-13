from curses.ascii import SO
from django import forms
from .models import Estatus, SolicitudesVacantes
from configuraciones.models import LocacionesPuestos, PuestosOperativos, Locaciones



class SolicitudesCreation(forms.ModelForm):
    locaciones =forms.ModelChoiceField(queryset=Locaciones.objects.filter(contactos__user_id=3).select_related(), to_field_name="id",)
    locaciones_puestos =forms.ModelChoiceField(queryset=LocacionesPuestos.objects.filter(locaciones_id=2), empty_label="-- Hola --", to_field_name="id",)

    
    class Meta:
        model = SolicitudesVacantes
        fields = ['locaciones','locaciones_puestos','cantidad','sueldos','periodo_pago','comiciones','bono','garantia','user']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Locación',
        })
        self.fields['locaciones_puestos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Locación',
        })
        self.fields['cantidad'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Cantidad',
        })
        self.fields['sueldos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'sueldo',
        })
        self.fields['periodo_pago'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'periodo_pago',
        })
        self.fields['comiciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'comiciones',
        })
        self.fields['bono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'bono',
        })
        self.fields['garantia'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'garantia',
        })
        self.fields['user'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'user_id',
        })