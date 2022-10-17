from django.shortcuts import render, redirect

import solicitudes
from .models import SolicitudesVacantes, SolicitudesEstatus, Estatus
from .forms import SolicitudesForm, EstatusForm

# Create your views here.
"""Gestion de las Solicitudes de Vacantes"""

def solicitudesView(request):
    """Vista que gestiona la información de las entidades"""
    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Gestión de solicitudes de vacantes.'}
    solicitudes = SolicitudesVacantes.objects.filter(activo='Y')
    return render(request,"solicitudes/solicitudes.html",{"titles":titles, "solicitudes":solicitudes})



def createSolicitudes(request):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Nueva Solicitud.'}
    if request.method == "POST":
        formulario = SolicitudesForm(request.POST or None)
        if formulario.is_valid():
            solicitud = formulario.save()
            estatus = Estatus.objects.get(tipos='solicitud',estatus='Abierta')

            solicitud_estatus = SolicitudesEstatus.objects.create(solicitudes_vacantes=solicitud,estatus=estatus)
            solicitud_estatus.save()
            return redirect('DetailsSolicitudes', id=solicitud.id)
    
    formulario = SolicitudesForm()
       
    return render(request,"solicitudes/create_solicitud.html",{"titles":titles, "formulario":formulario})


def editSolicitudes(request, id):
    """Vista que permite editar la infiormación de las solicitudes"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Editar información de la solicitud.'}
    solicitudes = SolicitudesVacantes.objects.get(id=id)
    if request.method == "POST":
        formulario = SolicitudesForm(request.POST or None, instance=solicitudes)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsSolicitudes',id=id)
    else:
        formulario = SolicitudesForm(instance=solicitudes)

    return render(request,"solicitudes/create_solicitud.html",{"titles":titles, "formulario":formulario, "id":id})



def detailsSolicitudes(request, id):
    """Vista del datalle de la vacante y gestiona la información de los candidatos"""    

    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la vacante.'}
    solicitud = SolicitudesVacantes.objects.get(id=id)
    estatus = SolicitudesEstatus.objects.get(solicitudes_vacantes_id=id, activo='Y')
    return render(request,"solicitudes/details_solicitud.html",{
        "titles":titles, 
        "solicitud":solicitud, 
        "estatus":estatus,
    })



"""Catalogo de los estatus"""

def estatusView(request):
    """Vista que gestiona la información de los estutus para las solicitudes y los candidatos"""
    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Catalogo de  estatus.'}
    estatus = Estatus.objects.filter(activo='Y')
    return render(request,"solicitudes/estatus.html",{"titles":titles, "estatus":estatus})



def createEstatus(request):
    """Vista que permite agregar nuevos estados, para solicitudes y para los candidatos"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Nuevo Estatus.'}
    if request.method == "POST":
        formulario = EstatusForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Estatus')
    
    formulario = EstatusForm()
       
    return render(request,"solicitudes/create_estatus.html",{"titles":titles, "formulario":formulario})



def editEstatus(request, id):
    """Esta vista permite editar la informacion de un estatus"""
    titles = {"title_page":'Solicitudes',"sub_title_page":'Editar información del puesto.'}
    estatus = Estatus.objects.get(id=id)
    if request.method == "POST":
        formulario = EstatusForm(request.POST or None, instance=estatus)
        if formulario.is_valid():
            formulario.save()
            return redirect('Estatus')
    else:
        formulario = EstatusForm(instance=estatus)

    return render(request,"solicitudes/create_estatus.html",{"titles":titles, "formulario":formulario, "id":id})