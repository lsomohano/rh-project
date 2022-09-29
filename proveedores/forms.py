from django import forms
from .models import Proveedores, ContactosProveedores, LocacionesProveedores

class ProveedoresCreation(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['proveedor','rfc','razon_social','direccion','codigo_postal','telefono','email','activo']
    
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


class ContactosProveedoresCreation(forms.Form):
    class Meta:
        model = ContactosProveedores
        fields = ['contacto_nombre','proveedores','telefono','email','tipo_contacto','activo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['contacto_nombre'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Nombre de Contacto',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Telefono',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })
        self.fields['tipo_contacto'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Tipo de Contacto',
        })
        self.fields['activo'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Activo',
        })