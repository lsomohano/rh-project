from django.shortcuts import render, redirect
from .models import Facturas, FacturasCandidatos
from solicitudes.models import Candidatos
from .forms import FacturacionForm

# Create your views here.

def facturasView(request):
    """Vista principal del modulo de facturas, 
    en este modulo se generan los reportes de los candidatos contratados que los proveedores podran facturar
    """
    
    titles = {"title_page":'Facturas',"sub_title_page":'Lista de facturas.'}
    facturas = Facturas.objects.filter(activo='Y')
    return render(request,"facturacion/facturacion.html",{"titles":titles, "solicitudes":facturas})


def createFacturacion(request):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Faturación',"sub_title_page":'Nuevo proceso de facturación.'}
    if request.method == "POST":
        formulario = FacturacionForm(request.POST or None)
        if formulario.is_valid():
            facturacion = formulario.save()
            return redirect('DetailsFacturacion', id=facturacion.id)
    
    formulario = FacturacionForm()

    return render(request,"facturacion/create_facturacion.html",{"titles":titles, "formulario":formulario})


def detailsFacturacion(request, id):
    """Vista de permite ver los detalles de una factura,
    como candidatos facturdos, y la """    

    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la vacante.'}
    facturacion = Facturas.objects.get(id=id)

    #candidatos = Candidatos.objects.filter(solicitudes_vacantes_id=id).select_related('personas').prefetch_related('id__candidatos_estatus')
    #candidatos = Candidatos.objects.raw("""SELECT c.id, c.created, c.aceptado, c.personas_id, p.nombre, p.apellido_paterno,p.apellido_materno, p.rfc, p.fecha_nacimiento, p.email, p.genero, ce.created AS fecha_estatus, e.estatus, e.descripcion FROM candidatos c
                                            #INNER JOIN personas p ON p.id=c.personas_id
                                            #INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
                                           # INNER JOIN calogos_estatus e ON e.id=ce.estatus_id
                                            #WHERE c.solicitudes_vacantes_id=%s""",(id,))
                                                

    return render(request,"facturacion/details_facturacion.html",{
        "titles":titles, 
        "facturacion":facturacion
    })


def createFacturasCandidatos(request):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Faturación',"sub_title_page":'Agregar candidatos al reporte.'}
    if request.method == "POST":
        formulario = FacturacionForm(request.POST or None)
        if formulario.is_valid():
            facturacion = formulario.save()
            return redirect('DetailsFacturacion', id=facturacion.id)
    
    candidatos = Cand
    formulario = FacturacionForm()

    return render(request,"facturacion/create_facturacion.html",{"titles":titles, "formulario":formulario})
