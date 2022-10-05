from django import forms
from .models import Proveedores, ContactosProveedores, LocacionesProveedores

class ProveedoresCreation(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['proveedor','rfc','razon_social','direccion','codigo_postal','telefono','email']
        widgets = {
            'id': forms.HiddenInput(),
        }

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
        


class ContactosProveedoresCreation(forms.ModelForm):
    class Meta:
        model = ContactosProveedores
        fields = ['user','proveedores','telefono','tipo_contacto']
        widgets = {
            'proveedores': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Proveedor',
            'readonly':'readonly',
        })
        self.fields['user'].widget.attrs.update({
            'class':'form-control select2bs4',
            'placeholder':'user',
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Telefono',
        })
        self.fields['tipo_contacto'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Tipo de Contacto',
        })

class LocacionesProveedoresCreation(forms.ModelForm):
    class Meta:
        model = LocacionesProveedores
        fields = ['locaciones','proveedores']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control select2bs4',
            'placeholder':'locaciones',
        })

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'proveedores',
        })
        
        