from django import forms
from .models import Proveedores, ContactosProveedores, LocacionesProveedores

class ProveedoresCreation(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['id','proveedor','rfc','razon_social','direccion','codigo_postal','telefono','email']
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
        fields = ['contacto_nombre','proveedores','telefono','email','tipo_contacto']
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

class LocacionesProveedoresCreation(forms.ModelForm):
    class Meta:
        model = LocacionesProveedores
        fields = ['locaciones','proveedores']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['locaciones'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'locaciones',
        })

        self.fields['proveedores'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'proveedores',
        })
        
        