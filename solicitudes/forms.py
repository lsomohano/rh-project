from curses.ascii import SO
from django import forms
from .models import Candidatos, Estatus, Personas, SolicitudesVacantes
from configuraciones.models import LocacionesPuestos, PuestosOperativos, Locaciones



class SolicitudesForm(forms.ModelForm):

    locaciones = forms.ModelChoiceField(queryset=Locaciones.objects.all(), empty_label="-- Locaciones --", to_field_name="id",)
    puestos_operativos = forms.ModelChoiceField(queryset=PuestosOperativos.objects.all(), empty_label="-- Puestos --", to_field_name="id",)
    
    class Meta:
        model = SolicitudesVacantes
        fields = ['locaciones','puestos_operativos','cantidad','sueldos','periodo_pago','comiciones','bono','garantia','user']
        widgets = {
            'user': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Locación',
        })
        self.fields['puestos_operativos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Puesto',
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


class PersonasForm(forms.ModelForm):    
    class Meta:
        model = Personas
        fields = ['rfc','nombre','apellido_paterno','apellido_materno','fecha_nacimiento','email','telefono','cv_solicitud']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre',
        })
        self.fields['apellido_paterno'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Apellido Paterno',
        })
        self.fields['apellido_materno'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Apellido Materno',
        })
        self.fields['rfc'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'R.F.C.',
        })
        self.fields['fecha_nacimiento'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'data-target':"#fecha_nacimiento",
            'placeholder':'Fecha Nacimiento',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Telefono',
        })
        self.fields['cv_solicitud'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'CV o Solicitud de empleo',
        })
        

class CandidatosForm(forms.ModelForm):  

    class Meta:
        model = Candidatos
        fields = ['reporte_entrevista','evaluacion_psicometrica','solicitudes_vacantes','user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['reporte_entrevista'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'reporte_entrevista',
        })
        self.fields['evaluacion_psicometrica'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'evaluacion_psicometrica',
        })
        