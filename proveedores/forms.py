from django import forms
from .models import Proveedores

class ProveedoresCreation(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['proveedor','rfc','razon_social','direccion','codigo_postal','telefono','email','activo','id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedor'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre Proveedor',
        })
        self.fields['rfc'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'R.F.C.',
        })
        self.fields['razon_social'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Razón Social',
        })
        self.fields['direccion'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Dirección completa',
        })
        self.fields['codigo_postal'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Codigo Postal',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Numero Telefonico',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Dirección email',
        })
        self.fields['activo'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Activo',
        })

    #proveedor = forms.CharField(required=True, label='Proveedor')
    #proveedor = forms.CharField(label='Proveedor', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Proveedor'}) )
    #rfc = forms.CharField(label='R.F.C.', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'R.F.C.'}) )
    #razon_social = forms.CharField(label='Razon Social', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}) )
    #direccion = forms.CharField(label='Proveedor', required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Dirección Complta'}) )
    #codigo_postal = forms.CharField(label='Codigo Postal', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Proveedor'}) )
    #telefono = forms.CharField(label='Telefono', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}) )
    #email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}) )
    #activo = forms.Select(choices=[(tag.name, tag.value) for tag in activo], widget=forms.Select(attrs={'class':'form-control','placeholder':'Activo'}) )