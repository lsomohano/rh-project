import email
from django import forms
from .models import activo

class ProveedoresCreation(forms.Form):
    #proveedor = forms.CharField(required=True, label='Proveedor')
    proveedor = forms.CharField(label='Proveedor', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Proveedor'}) )
    rfc = forms.CharField(label='R.F.C.', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'R.F.C.'}) )
    razon_social = forms.CharField(label='Razon Social', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}) )
    direccion = forms.CharField(label='Proveedor', required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Dirección Complta'}) )
    codigo_postal = forms.CharField(label='Codigo Postal', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Proveedor'}) )
    telefono = forms.CharField(label='Proveedor', required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono'}) )
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}) )
    activo = forms.CharField(label='Proveedor', required=True, widget=forms.Select(attrs={'class':'form-control','placeholder':'Proveedor','choices':activo}) )