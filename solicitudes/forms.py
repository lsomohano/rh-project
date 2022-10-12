from curses.ascii import SO
from django import forms
from .models import Estatus, SolicitudesVacantes
from configuraciones.models import LocacionesPuestos, PuestosOperativos



class SolicitudesCreation(forms.ModelForm):
    locaciones_puestos =forms.ModelChoiceField(queryset=LocacionesPuestos.objects.filter(locaciones_id=1), empty_label="-- Hola --", to_field_name="id",)
    
    class Meta:
        model = SolicitudesVacantes
        fields = ['locaciones','locaciones_puestos']
        

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