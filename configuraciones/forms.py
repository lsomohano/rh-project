from django import forms
from .models import Ciudades, Entidades, Locaciones, PuestosNominas, PuestosOperativos, Contactos, LocacionesPuestos 

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
            'class':'form-control select2bs4',
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
            'class':'form-control select2bs4',
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
            'class':'form-control select2bs4',
            'placeholder':'Puesto nomina',
        })
        self.fields['canal_reclutamiento'].widget.attrs.update({
            'class':'form-control select2bs4',
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
            'class':'form-control select2bs4',
            'placeholder':'Ciudad',
        })
        self.fields['zona_ciudad'].widget.attrs.update({
            'class':'form-control select2bs4',
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

class ContactosLocacionesCreation(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['user','locaciones','horario_inicio','horario_termino','dias_atencion']
        widgets = {
            'locaciones': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Proveedor',
            'readonly':'readonly',
        })
        self.fields['user'].widget.attrs.update({
            'class':'form-control select2bs4',
            'placeholder':'User',
        })
        self.fields['horario_inicio'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'horario_inicio',
        })
        self.fields['horario_termino'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'horario_termino',
        })
        self.fields['dias_atencion'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'dias_atencion',
        })

class PuestosLocacionesCreation(forms.ModelForm):
    class Meta:
        model = LocacionesPuestos
        fields = ['puestos_operativos','locaciones','staf_requerido','staf_contratado']
        widgets = {
            'locaciones': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Proveedor',
            'readonly':'readonly',
        })
        self.fields['puestos_operativos'].widget.attrs.update({
            'class':'form-control select2bs4',
            'placeholder':'Puestos operativos',
        })
        self.fields['staf_requerido'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Staff requerido',
        })
        self.fields['staf_contratado'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Staff contratado',
        })