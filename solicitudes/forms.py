from curses.ascii import SO
from django import forms
from .models import Estatus, SolicitudesVacantes
from configuraciones.models import LocacionesPuestos, PuestosOperativos, Locaciones



class SolicitudesForm(forms.ModelForm):

    locaciones = forms.ModelChoiceField(queryset=Locaciones.objects.all(), empty_label="-- Locaciones --", to_field_name="id",)
    locaciones_puestos = forms.ModelChoiceField(queryset=LocacionesPuestos.objects.filter(locaciones_id=1), empty_label="-- Puestos --", to_field_name="id",)

    
    class Meta:
        model = SolicitudesVacantes
        fields = ['locaciones','locaciones_puestos','cantidad','sueldos','periodo_pago','comiciones','bono','garantia','user']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('users')
        super().__init__(*args, **kwargs)

        qs = Locaciones.objects.filter(contactos__user_id=self.user).select_related()
        self.fields['locaciones'].queryset = qs

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

class EstatusForm(forms.ModelForm):    
    class Meta:
        model = Estatus
        fields = ['estatus','descripcion','tipos',]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estatus'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'estatus',
        })
        self.fields['descripcion'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'descripcion',
        })
        self.fields['tipos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'tipos',
        })