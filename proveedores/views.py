from django.shortcuts import render, redirect
from .models import Proveedores, ContactosProveedores, LocacionesProveedores
from .forms import ProveedoresCreation, ContactosProveedoresCreation, LocacionesProveedoresCreation
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="Log_In")
def proveedores(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Gestión de info de Provedores.'}
    proveedores = Proveedores.objects.filter(activo='Y')

    return render(request,"proveedores/proveedores.html",{"titles":titles, "proveedores":proveedores})


@login_required(login_url="Log_In")
def createView(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Nuevo proveedor.'}
    if request.method == "POST":
        formulario = ProveedoresCreation(request.POST or None)
        if formulario.is_valid():
            proveedor= formulario.save()
            return redirect('Details',id=proveedor.id)
    
    formulario = ProveedoresCreation()
       
    return render(request,"proveedores/create.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def editView(request, id):

    titles = {"title_page":'Proveedores',"sub_title_page":'Editar información del proveedor.'}
    proveedor = Proveedores.objects.get(id=id)
    if request.method == "POST":
        formulario = ProveedoresCreation(request.POST or None, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect('Details',id=id)
    else:
        formulario = ProveedoresCreation(instance=proveedor)

    return render(request,"proveedores/edit.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def detailsView(request, id):
    
    titles = {"title_page":'Proveedores',"sub_title_page":'Información del proveedor.'}
    proveedor = Proveedores.objects.get(id=id)
    contactos = ContactosProveedores.objects.filter(proveedores_id=id, activo='Y')
    locaciones = LocacionesProveedores.objects.filter(proveedores_id=id, activo='Y').select_related('locaciones')

    return render(request,"proveedores/details.html",{
        "titles":titles, 
        "proveedor":proveedor, 
        "contactos":contactos, 
        "locaciones":locaciones})


@login_required(login_url="Log_In")
def deleteView(request, id):

    proveedor = Proveedores.objects.get(id=id)
    proveedor.activo='N'
    proveedor.save()

    return redirect('Proveedores')


"""
Vistas que controlan los evnetos de los contactos de los proveedores

"""

@login_required(login_url="Log_In")
def createContactosView(request,proveedores_id):
    
    titles = {"title_page":'Proveedores',"sub_title_page":'Agregar nuevo contacto.'}
    if request.method == "POST":
        formulario = ContactosProveedoresCreation(request.POST or None)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('Details',id=proveedores_id)
    
    formulario = ContactosProveedoresCreation()
    return render(request,"proveedores/create_contacto.html", {"titles":titles, "formulario":formulario,"proveedores_id":proveedores_id})


@login_required(login_url="Log_In")
def editContactosView(request, id):

    titles = {"title_page":'Proveedores',"sub_title_page":'Editar información del contactos.'}
    contacto = ContactosProveedores.objects.get(id=id)
    if request.method == "POST":
        formulario = ContactosProveedoresCreation(request.POST or None, instance=contacto)
        if formulario.is_valid():
            proveedores_id = formulario['proveedores'].value()
            formulario.save()
            return redirect('Details',id=proveedores_id)
    else:
        formulario = ContactosProveedoresCreation(instance=contacto)

    return render(request,"proveedores/edit_contacto.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def DeleteContactosView(request, id):

    contacto = ContactosProveedores.objects.get(id=id)
    
    proveedores_id = contacto.proveedores_id
    contacto.activo='N'
    contacto.save()

    return redirect('Details',id=proveedores_id)

"""Sección de gestion de las locaciones asignadas"""

@login_required(login_url="Log_In")
def createLocacionesViews(request, proveedores_id):
    titles = {"title_page":'Proveedores',"sub_title_page":'Agregar nuevo contacto.'}
    if request.method == "POST":
        formulario = LocacionesProveedoresCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Details',id=proveedores_id)
    
    formulario = LocacionesProveedoresCreation()

    return render(request,"proveedores/create_locacion.html", {"titles":titles, "formulario":formulario,"proveedores_id":proveedores_id})


@login_required(login_url="Log_In")
def DeleteLocacionesView(request, id):

    locacion = LocacionesProveedores.objects.get(id=id)
    
    proveedores_id = locacion.proveedores_id
    locacion.activo='N'
    locacion.save()

    return redirect('Details',id=proveedores_id)