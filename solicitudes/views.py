from django.shortcuts import render, redirect

import solicitudes
from .models import SolicitudesVacantes
from .forms import SolicitudesCreation

# Create your views here.

def solicitudesView(request):
    """Vista que gestiona la información de las entidades"""
    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Gestión de solicitudes de vacantes.'}
    solicitudes = SolicitudesVacantes.objects.filter(activo='Y')
    return render(request,"solicitudes/solicitudes.html",{"titles":titles, "solicitudes":solicitudes})


def createSolicitudes(request):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Entidades',"sub_title_page":'Nueva entidad.'}
    if request.method == "POST":
        formulario = SolicitudesCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Solicitudes')
    
    formulario = SolicitudesCreation()
       
    return render(request,"solicitudes/create_solicitud.html",{"titles":titles, "formulario":formulario})


def detailsSolicitudes(request, id):
    """Vista del datalle de la vacante, tambien se gestiona la información de los candidatos"""    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la vacante.'}
    solicitud = SolicitudesVacantes.objects.get(id=id)
    #puestos_operativos = PuestosOperativos.objects.filter(puestos_nominas_id=id, activo='Y')

    return render(request,"solicitudes/details_solicitud.html",{
        "titles":titles, 
        "solicitud":solicitud, 
    })