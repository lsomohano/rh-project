from curses.ascii import SO
from django import forms
from .models import Candidatos, Entrevistas, Estatus, Personas, SolicitudesVacantes
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
        fields = ['rfc','nombre','apellido_paterno','apellido_materno','fecha_nacimiento','genero','email','telefono']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['rfc'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'R.F.C.',
        })
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
        self.fields['fecha_nacimiento'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'data-target':"#fecha_nacimiento",
            'placeholder':'Fecha Nacimiento',
        })
        self.fields['genero'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Genero',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Telefono',
        })
        
        

class CandidatosForm(forms.ModelForm):  

    class Meta:
        model = Candidatos
        fields = ['cv_solicitud','reporte_entrevista','evaluacion_psicometrica','referencias','solicitudes_vacantes','user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cv_solicitud'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'CV o Solicitud de empleo',
        })
        self.fields['reporte_entrevista'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'reporte_entrevista',
        })
        self.fields['evaluacion_psicometrica'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'evaluacion_psicometrica',
        })
        self.fields['referencias'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'referencias',
        })

class EntrevistasForm(forms.ModelForm):  

    class Meta:
        model = Entrevistas
        fields = ['fecha_programada','hora_programada','indicaciones','candidatos']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha programada',
             'data-target':"#fecha_programada",
        })
        self.fields['hora_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Hora Programada',
            'data-target':'#hora_programada'
        })
        self.fields['indicaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Indicaciones para la entrevista',
        })
        self.fields['candidatos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Candidato',
        })

class Entrevistas2Form(forms.ModelForm):  

    class Meta:
        model = Entrevistas
        fields = ['asistio','fecha_entrevista','fecha_programada','hora_programada','indicaciones','candidatos']
        labels = {
            "asistio":"¿Asistio?"
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha programada',
             'data-target':"#fecha_programada",
        })
        self.fields['hora_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Hora Programada',
            'data-target':'#hora_programada'
        })
        self.fields['indicaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Indicaciones para la entrevista',
        })
        self.fields['candidatos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Candidato',
        })
        self.fields['fecha_entrevista'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha entrevista',
            'data-target':"#fecha_entrevista",
            'readonly':"readonly"
        })
        self.fields['asistio'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Asistio',
        })


class Entrevistas3Form(forms.ModelForm):  

    class Meta:
        model = Entrevistas
        fields = ['asistio','fecha_entrevista','fecha_programada','hora_programada','indicaciones','candidatos']
        labels = {
            "fecha_entrevista": "Fecha Contratación",
            "asistio":"¿Contrató?"
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha programada',
            'data-target':"#fecha_programada",
        })
        self.fields['hora_programada'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Hora Programada',
            'data-target':'#hora_programada'
        })
        self.fields['indicaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Indicaciones para la entrevista',
        })
        self.fields['candidatos'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Candidato',
        })
        self.fields['fecha_entrevista'].widget.attrs.update({
            'class':'form-control datetimepicker-input',
            'placeholder':'Fecha contratación',
            'data-target':"#fecha_entrevista",
            'readonly':"readonly"
        })
        self.fields['asistio'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Asistio',
        })