from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedores, ContactosProveedores
from .forms import ProveedoresCreation

# Create your views here.

def proveedores(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Gestión de info de Provedores.'}
    proveedores = Proveedores.objects.all()

    return render(request,"proveedores/proveedores.html",{"titles":titles, "proveedores":proveedores})


def createView(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Nuevo proveedor.'}
    if request.method == "POST":
        formulario = ProveedoresCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Proveedores')
    
    formulario = ProveedoresCreation()
       
    return render(request,"proveedores/create.html",{"titles":titles, "formulario":formulario})

def editView(request, id):
    titles = {"title_page":'Proveedores',"sub_title_page":'Editar proveedor.'}
    proveedor = Proveedores.objects.get(id=id)
    formulario = ProveedoresCreation(request.POST or None, instance=proveedor)
    if request.method == "POST":
        #formulario = ProveedoresCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Proveedores')
    
    return render(request,"proveedores/create.html",{"titles":titles, "formulario":formulario})