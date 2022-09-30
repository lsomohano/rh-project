from django import forms
from .models import Ciudades, Entidades, Locaciones, PuestosNominas, PuestosOperativos

class entidadesCreate(forms.ModelForm):
    class Meta:
        model = Entidades
        fields = ['entidad','pais']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['entidad'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre de Entidad',
        })
        self.fields['pais'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Pais',
        })


class ciudadesCreate(forms.ModelForm):
    class Meta:
        model = Ciudades
        fields = ['ciudad','entidades']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ciudad'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre de Ciudad',
        })
        self.fields['entidades'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Entidad',
        })

class puestosNominasCreate(forms.ModelForm):
    class Meta:
        model = PuestosNominas
        fields = ['puesto_nomina',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['puesto_nomina'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Puesto nomina',
        })

class puestosOperativosCreate(forms.ModelForm):
    class Meta:
        model = PuestosOperativos
        fields = ['puesto_operativo','puestos_nominas','canal_reclutamiento']
        widgets = {
            'puestos_nominas': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['puesto_operativo'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Puesto operativo',
        })
        self.fields['puestos_nominas'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Puesto nomina',
        })
        self.fields['canal_reclutamiento'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Recluatamiento',
        })


class LocacionesCreate(forms.ModelForm):
    class Meta:
        model = Locaciones
        fields = ['locacion','locacion_name','direccion','codigo_postal','ciudades','zona_ciudad','latitud','longitud','horario_apertura','horario_cierre','dias_operativos','telefono','email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locacion'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Locación',
        })
        self.fields['locacion_name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre de locación',
        })
        self.fields['direccion'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Dirección',
        })
        self.fields['codigo_postal'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Codigo Postal',
        })
        self.fields['ciudades'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Ciudad',
        })
        self.fields['zona_ciudad'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Zona',
        })
        self.fields['latitud'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'latitud',
        })
        self.fields['longitud'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'longitud',
        })
        self.fields['horario_apertura'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Hora de apertura',
        })
        self.fields['horario_cierre'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Hora de cierre',
        })
        self.fields['dias_operativos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Dias operativos',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Telefono',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })
        