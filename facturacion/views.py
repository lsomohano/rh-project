from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Facturas, FacturasCandidatos
from solicitudes.models import Candidatos
from .forms import FacturacionForm
from django.core.serializers import serialize

# Create your views here.

def facturasView(request):
    """Vista principal del modulo de facturas, 
    en este modulo se generan los reportes de los candidatos contratados que los proveedores podran facturar
    """
    
    titles = {"title_page":'Facturas',"sub_title_page":'Lista de facturas.'}
    facturas = Facturas.objects.filter(activo='Y')
    return render(request,"facturacion/facturacion.html",{"titles":titles, "facturas":facturas})


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

    candidatos = Candidatos.objects.raw(""" SELECT c.id, 
        p.rfc, p.nombre, p.apellido_paterno, p.apellido_materno, 
        ce.created AS estatus_fecha, ec.estatus, 
        u.first_name, u.last_name, 
        pr.rfc AS rfc_proveedor, 
        s.id AS solicitudes_id, 
        l.locacion, 
        po.puesto_operativo
        FROM candidatos c
        INNER JOIN personas p ON p.id=c.personas_id
        INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
        INNER JOIN calogos_estatus ec ON ec.id=ce.estatus_id
        INNER JOIN autenticacion_user u ON u.id=c.user_id
        INNER JOIN contactos_proveedores cp ON cp.user_id=u.id
        INNER JOIN proveedores pr ON pr.id=cp.proveedores_id 
        INNER JOIN solicitudes_vacantes s ON s.id=c.solicitudes_vacantes_id
        INNER JOIN locaciones l ON l.id=s.locaciones_id
        INNER JOIN puestos_operativos po ON po.id=s.puestos_operativos_id
        WHERE ec.estatus='Contratado' AND ce.created BETWEEN %s AND %s """,(facturacion.fecha_ini, facturacion.fecha_fin,))
                                                

    return render(request,"facturacion/details_facturacion.html",{
        "titles":titles, 
        "facturacion":facturacion,
        "candidatos":candidatos,
    })


def addCandidatos(request,fecha_ini,fecha_fin):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Faturación',"sub_title_page":'Agregar candidatos al reporte.'}
    if request.method == "POST":
        formulario = FacturacionForm(request.POST or None)
        if formulario.is_valid():
            facturacion = formulario.save()
            return redirect('DetailsFacturacion', id=facturacion.id)
    
    candidatos = Candidatos.objects.raw(""" SELECT c.id, 
        p.rfc, p.nombre, p.apellido_paterno, p.apellido_materno, 
        ce.created AS estatus_fecha, ec.estatus, 
        u.first_name, u.last_name, 
        pr.rfc as rfc_proveedor, 
        s.id AS solicitudes_id, 
        l.locacion, 
        po.puesto_operativo
        FROM candidatos c
        INNER JOIN personas p ON p.id=c.personas_id
        INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
        INNER JOIN calogos_estatus ec ON ec.id=ce.estatus_id
        INNER JOIN autenticacion_user u ON u.id=c.user_id
        INNER JOIN contactos_proveedores cp ON cp.user_id=u.id
        INNER JOIN proveedores pr ON pr.id=cp.proveedores_id 
        INNER JOIN solicitudes_vacantes s ON s.id=c.solicitudes_vacantes_id
        INNER JOIN locaciones l ON l.id=s.locaciones_id
        INNER JOIN puestos_operativos po ON po.id=s.puestos_operativos_id
        WHERE ec.estatus='Contratado' AND ce.created BETWEEN %s AND %s """,(fecha_ini, fecha_fin,))
        
    formulario = FacturacionForm()

    return render(request,"facturacion/add_candidatos.html",{"titles":titles, "candidatos":candidatos})


def listCandidatosJson(request,fecha_ini,fecha_fin):
    
    candidatos = serialize('json', Candidatos.objects.raw(""" SELECT c.id, 
        p.rfc, p.nombre, p.apellido_paterno, p.apellido_materno, 
        ce.created AS estatus_fecha, ec.estatus, 
        u.first_name, u.last_name, 
        pr.rfc as rfc_proveedor, 
        s.id AS solicitudes_id, 
        l.locacion, 
        po.puesto_operativo
        FROM candidatos c
        INNER JOIN personas p ON p.id=c.personas_id
        INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
        INNER JOIN calogos_estatus ec ON ec.id=ce.estatus_id
        INNER JOIN autenticacion_user u ON u.id=c.user_id
        INNER JOIN contactos_proveedores cp ON cp.user_id=u.id
        INNER JOIN proveedores pr ON pr.id=cp.proveedores_id 
        INNER JOIN solicitudes_vacantes s ON s.id=c.solicitudes_vacantes_id
        INNER JOIN locaciones l ON l.id=s.locaciones_id
        INNER JOIN puestos_operativos po ON po.id=s.puestos_operativos_id
        WHERE ec.estatus='Contratado' AND ce.created BETWEEN %s AND %s """,(fecha_ini, fecha_fin,)))

    return HttpResponse(candidatos,'application/json')