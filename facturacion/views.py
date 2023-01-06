from django.shortcuts import render, redirect
from .models import Facturas, FacturasCandidatos
from solicitudes.models import Candidatos, CandidatosEstatus, Estatus
from .forms import FacturacionForm, FacturacionPrefacturaForm, FacturacionfacturaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url="Log_In")
def facturasView(request):
    """Vista principal del modulo de facturas, 
    en este modulo se generan los reportes de los candidatos contratados que los proveedores podran facturar
    """
    
    titles = {"title_page":'Facturas',"sub_title_page":'Lista de facturas.'}
    facturas = Facturas.objects.filter(activo='Y')
    #Se comprueba si el ususario no pertenece un grupo
    for group in request.user.groups.all():
        #Si pertenece al grupo RH Gerentes se cambia los fiels locaciones y puestos operativos con los elementos que pueden ver.
        if group.name == 'Proveedores':
            facturas = facturas.filter(proveedores__contactosproveedores__user_id=request.user.id)
    return render(request,"facturacion/facturacion.html",{"titles":titles, "facturas":facturas})


@login_required(login_url="Log_In")
def createFacturacion(request):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Faturación',"sub_title_page":'Nuevo proceso de facturación.'}
    if request.method == "POST":
        formulario = FacturacionForm(request.POST or None)
        if formulario.is_valid():
            facturacion = formulario.save()
            messages.add_message(request=request,level=messages.SUCCESS, message="El periodo de facturación se creó correctamente.")
            return redirect('DetailsFacturacion', id=facturacion.id)
        else:
            messages.add_message(request=request,level=messages.ERROR, message="El periodo de facturación no se pudo crear.")
            for field, items in formulario.errors.items():
                for item in items:
                    messages.add_message(request=request,level=messages.ERROR, message="{}: {}".format(field, item))
            
            return redirect('Facturacion')

    formulario = FacturacionForm()

    return render(request,"facturacion/create_facturacion.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
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
        INNER JOIN catalogos_estatus ec ON ec.id=ce.estatus_id
        INNER JOIN autenticacion_user u ON u.id=c.user_id
        INNER JOIN contactos_proveedores cp ON cp.user_id=u.id
        INNER JOIN proveedores pr ON pr.id=cp.proveedores_id 
        INNER JOIN solicitudes_vacantes s ON s.id=c.solicitudes_vacantes_id
        INNER JOIN locaciones l ON l.id=s.locaciones_id
        INNER JOIN puestos_operativos po ON po.id=s.puestos_operativos_id
        INNER JOIN facturas_candidatos fc ON fc.candidatos_id=c.id
        WHERE fc.activo='Y' AND fc.facturas_id=%s """,(id,))
                                                
    fc = FacturasCandidatos.objects.filter(facturas_id=id).count()
    return render(request,"facturacion/details_facturacion.html",{
        "titles":titles, 
        "facturacion":facturacion,
        "candidatos":candidatos,
        "fc":fc,
    })


@login_required(login_url="Log_In")
def addCandidatos(request,proveedores_id,facturas_id,fecha_ini,fecha_fin):
    """Vista que permite agregar nuevas solicitudes"""

    titles = {"title_page":'Faturación',"sub_title_page":'Agregar candidatos al reporte.'}

    if request.method == "POST":
        #factura = request.POST.getlist('facturas_id')
        if request.POST.getlist('partidas[]'):
            FacturasCandidatos.objects.filter(facturas_id=facturas_id).update(activo='N')
            for candidato in request.POST.getlist('partidas[]'): 
                
                if FacturasCandidatos.objects.filter(facturas_id=facturas_id, candidatos_id=candidato).exists():
                    FacturasCandidatos.objects.filter(facturas_id=facturas_id, candidatos_id=candidato).update(activo='Y')
                else:
                    can = FacturasCandidatos.objects.create(facturas_id=facturas_id, candidatos_id=candidato)
                    can.save()
            
                CandidatosEstatus.objects.filter(candidatos_id=candidato).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Facturación')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato, estatus_id=estatus.id)
                ce.save()

            messages.add_message(request=request,level=messages.SUCCESS, message="Los candidatos se agregaron correctamente al proceso de facturación.")
            
        else:
            messages.add_message(request=request,level=messages.WARNING, message="No se envió ningún candidato de la lista.")

        return redirect('DetailsFacturacion', id=facturas_id)

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
        INNER JOIN catalogos_estatus ec ON ec.id=ce.estatus_id
        INNER JOIN autenticacion_user u ON u.id=c.user_id
        INNER JOIN contactos_proveedores cp ON cp.user_id=u.id
        INNER JOIN proveedores pr ON pr.id=cp.proveedores_id AND pr.id=%s
        INNER JOIN solicitudes_vacantes s ON s.id=c.solicitudes_vacantes_id
        INNER JOIN locaciones l ON l.id=s.locaciones_id
        INNER JOIN puestos_operativos po ON po.id=s.puestos_operativos_id
        WHERE ec.estatus='Contratado' AND ce.created BETWEEN %s AND %s """,(proveedores_id,fecha_ini, fecha_fin,))   

    return render(request,"facturacion/add_candidatos.html",{"titles":titles, "candidatos":candidatos, "facturas_id":facturas_id})


@login_required(login_url="Log_In")
def addPrefactura(request,id):
    """Vista que permite agregar nuevas solicitudes"""
    
    titles = {"title_page":'Faturación',"sub_title_page":'Agregar Pre-Factura.'}
    facturacion = Facturas.objects.get(id=id)

    if request.method == "POST":
        formulario = FacturacionPrefacturaForm(request.POST, request.FILES, instance=facturacion)
        if formulario.is_valid():
            facturacion = formulario.save()
            messages.add_message(request=request,level=messages.SUCCESS, message="La pre factura se agregó correctamente.")
        else:
            messages.add_message(request=request,level=messages.WARNING, message="La pre factura no se pudo agregar.")
            for field, items in formulario.errors.items():
                for item in items:
                    messages.add_message(request=request,level=messages.ERROR, message="{}: {}".format(field, item))

        return redirect('DetailsFacturacion', id=id)

    formulario = FacturacionPrefacturaForm(instance=facturacion)

    return render(request,"facturacion/create_facturacion.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def addFactura(request,id):
    """Vista que permite agregar nuevas solicitudes"""
    
    titles = {"title_page":'Faturación',"sub_title_page":'Agregar Pre-Factura.'}
    facturacion = Facturas.objects.get(id=id)

    if request.method == "POST":
        formulario = FacturacionfacturaForm(request.POST, request.FILES, instance=facturacion)
        if formulario.is_valid():
            facturacion = formulario.save()

            fc = FacturasCandidatos.objects.filter(facturas_id=facturacion.id)
            for candidato in fc:
                CandidatosEstatus.objects.filter(candidatos_id=candidato.candidatos_id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Facturado')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato.candidatos_id, estatus_id=estatus.id)
                ce.save()

            messages.add_message(request=request,level=messages.SUCCESS, message="La factura se agregó correctamente.")
        else:
            messages.add_message(request=request,level=messages.WARNING, message="La factura no se pudo agregar.")
            for field, items in formulario.errors.items():
                for item in items:
                    messages.add_message(request=request,level=messages.ERROR, message="{}: {}".format(field, item))

        return redirect('DetailsFacturacion', id=id)
    
    formulario = FacturacionfacturaForm(instance=facturacion)

    return render(request,"facturacion/create_facturacion.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def paymentFactura(request, id):
    """Vista que permite cambiar la bendera a pagado Y """
    factura = Facturas.objects.get(id=id)
    factura.pagado='Y'
    factura.save()
    messages.add_message(request=request,level=messages.SUCCESS, message="La factura fue pagada.")
    return redirect('DetailsFacturacion', id=factura.id)
