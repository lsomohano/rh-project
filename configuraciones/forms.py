from django import forms
from .models import Entidades

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