from django.shortcuts import render, redirect
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
    titles = {"title_page":'Proveedores',"sub_title_page":'Editar información del proveedor.'}
    proveedor = Proveedores.objects.get(id=id)
    if request.method == "POST":
        formulario = ProveedoresCreation(request.POST or None, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect('Proveedores')
    else:
        formulario = ProveedoresCreation(instance=proveedor)

    return render(request,"proveedores/edit.html",{"titles":titles, "formulario":formulario})

def detailsView(request, id):
    
    titles = {"title_page":'Proveedores',"sub_title_page":'Información del proveedor.'}
    proveedor = Proveedores.objects.get(id=id)

    return render(request,"proveedores/details.html",{"titles":titles, "proveedor":proveedor})