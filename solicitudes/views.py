from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .models import Candidatos, Entrevistas, Personas, SolicitudesVacantes, SolicitudesEstatus, Estatus, CandidatosEstatus, Documentos, CandidatosDocumentos
from configuraciones.models import Locaciones, PuestosOperativos, LocacionesPuestos, Contactos
from .forms import CandidatosForm, EntrevistasForm, PersonasForm, SolicitudesForm, EstatusForm, Entrevistas2Form, Entrevistas3Form, EstatusCandidatosForm, IngresoForm, EstatusSolicitudesForm, AgendaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize

from django.utils import timezone
import datetime

# Create your views here.
"""Gestion de las Solicitudes de Vacantes"""

@login_required(login_url="Log_In")
def solicitudesView(request):
    """Vista que gestiona la información de las entidades"""
    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Gestión de solicitudes de vacantes.'}

    solicitudes = SolicitudesVacantes.objects.filter(activo='Y')
    #Se comprueba si el ususario no pertenece al grupo RH Gerentes
    for group in request.user.groups.all():
        #Si pertenece al grupo RH Gerentes se cambia los fiels locaciones y puestos operativos con los elementos que pueden ver.
        if group.name == 'Proveedores':
            solicitudes = solicitudes.filter(locaciones__locacionesproveedores__proveedores__contactosproveedores__user_id=request.user.id)
        if group.name == 'RH Gerentes':
            solicitudes = solicitudes.filter(locaciones__contactos__user_id=request.user.id)
            
    
    return render(request,"solicitudes/solicitudes.html",{"titles":titles, "solicitudes":solicitudes})


@login_required(login_url="Log_In")
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

    #Se comprueba si el ususario no pertenece al grupo RH Gerentes
    for group in request.user.groups.all():
        #Si pertenece al grupo RH Gerentes se cambia los fiels locaciones y puestos operativos con los elementos que pueden ver.
        if group.name == 'RH Gerentes':
            formulario.fields['locaciones'].queryset = Locaciones.objects.filter(contactos__user_id=request.user.id).select_related()
            formulario.fields['puestos_operativos'].queryset = PuestosOperativos.objects.filter(locacionespuestos__locaciones__contactos__user_id=request.user.id)
    
        
    return render(request,"solicitudes/create_solicitud.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
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


@login_required(login_url="Log_In")
def detailsSolicitudes(request, id):
    """Vista del datalle de la vacante y gestiona la información de los candidatos"""    

    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la vacante.'}

    solicitud = SolicitudesVacantes.objects.get(id=id)
    estatus = SolicitudesEstatus.objects.get(solicitudes_vacantes_id=id, activo='Y')
    contacto = Contactos.objects.get(user__id=solicitud.user_id)
    #candidatos = Candidatos.objects.filter(solicitudes_vacantes_id=id).select_related('personas').prefetch_related('id__candidatos_estatus')
    candidatos = Candidatos.objects.raw("""SELECT c.id, c.created, c.aceptado, c.personas_id, c.tipo_candidato, p.nombre, p.apellido_paterno,p.apellido_materno, p.rfc, p.fecha_nacimiento, p.email, p.genero, ce.created AS fecha_estatus, e.estatus, e.descripcion, en.tipo_evento, en.fecha_entrevista, en.asistio 
                                            FROM candidatos c
                                            INNER JOIN personas p ON p.id=c.personas_id
                                            INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
                                            INNER JOIN catalogos_estatus e ON e.id=ce.estatus_id
                                            LEFT JOIN entrevistas en ON en.candidatos_id=c.id AND en.tipo_evento='ingreso'
                                            WHERE c.solicitudes_vacantes_id=%s""",(id,))
                                                

    return render(request,"solicitudes/details_solicitud.html",{
        "titles":titles, 
        "solicitud":solicitud, 
        "contacto":contacto,
        "estatus":estatus,
        "candidatos":candidatos,
    })


@login_required(login_url="Log_In")
def deleteSolicitudes(request, id):
    """Vista que sirve para eliminar una solicitud, siempre y cuando su estatus sea 'Abierta' """
    solicitud = SolicitudesVacantes.objects.get(id=id)
    solicitud.activo='N'
    solicitud.save()

    SolicitudesEstatus.objects.filter(solicitudes_id=id).update(activo='N')
    estatus = Estatus.objects.get(tipos='solicitud',estatus='Eliminada')
    solicitud_estatus = SolicitudesEstatus.objects.create(solicitudes_vacantes=solicitud,estatus=estatus)
    solicitud_estatus.save()

    return redirect('Solicitudes')


def cancelSolicitudes(request, id):
    """Vista que permite cambiar a rechazado un candidato"""
    titles = {"title_page":'Solicitudes',"sub_title_page":'Cancelación de la solicitud.'}
    
    if request.method == "POST":
        formulario = EstatusSolicitudesForm(request.POST or None)
        if formulario.is_valid():
            
            SolicitudesEstatus.objects.filter(solicitudes_vacantes_id=id).update(activo='N')
            solicitud = SolicitudesVacantes.objects.get(id=id)

            solicitudestatus = formulario.save(commit=False)
            solicitudestatus.solicitudes_vacantes = solicitud
            solicitudestatus.estatus = Estatus.objects.get(tipos='solicitud',estatus='Cancelada')

            solicitudestatus.save()

            return redirect('DetailsSolicitudes', id=solicitudestatus.solicitudes_vacantes_id)
        else:
            return redirect('Home')


    formulario = EstatusSolicitudesForm()    
     
    return render(request,"solicitudes/create_rechazo.html",{"titles":titles, "formulario":formulario})
    


"""Catalogo de los estatus"""

@login_required(login_url="Log_In")
def estatusView(request):
    """Vista que gestiona la información de los estutus para las solicitudes y los candidatos"""
    
    titles = {"title_page":'Solicitudes',"sub_title_page":'Catalogo de  estatus.'}
    estatus = Estatus.objects.filter(activo='Y')
    return render(request,"solicitudes/estatus.html",{"titles":titles, "estatus":estatus})


@login_required(login_url="Log_In")
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


@login_required(login_url="Log_In")
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



##### Gestion de los candidatos #####


class CandidatosCreate(CreateView):
    """ Vista que permite agregar infomación de los candidatos """
    model = Candidatos
    template_name = "solicitudes/create_candidatos.html"
    form_class = CandidatosForm
    second_form_class = PersonasForm
    
    def get_form(self, form_class=None):
        solicitudes_id = self.kwargs.get('solicitudes_id')
        form = CandidatosForm()
        form.fields['candidato_sustituye'].queryset = Candidatos.objects.filter(solicitudes_vacantes_id=solicitudes_id).filter(candidatosestatus__activo='Y', candidatosestatus__estatus__estatus='rechazado')
        return form

    def get_context_data(self, **kwargs):
        context = super(CandidatosCreate, self).get_context_data(**kwargs)
        solicitudes_id = self.kwargs.get('solicitudes_id')
        
        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Nuevo Candidato.'}
        context['solicitudes_id'] = solicitudes_id
        context['documentos'] = Documentos.objects.filter(activo='Y')
           
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        solicitudes_id = self.kwargs.get('solicitudes_id')
        form = self.form_class(request.POST, request.FILES)
        form.fields['candidato_sustituye'].queryset = Candidatos.objects.filter(solicitudes_vacantes_id=solicitudes_id).filter(candidatosestatus__activo='Y', candidatosestatus__estatus__estatus='rechazado')
        form2 = self.second_form_class(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            candidato = form.save(commit=False)
            candidato.personas = form2.save()
            candidato.save()

            #Se asigna un estatus al candidato
            estatus = Estatus.objects.get(tipos='candidato', estatus='Postulado')
            candidatos_estatus = CandidatosEstatus.objects.create(candidatos=candidato, estatus=estatus)
            candidatos_estatus.save()

            if request.POST.getlist('documentos[]'):
                for documento in request.POST.getlist('documentos[]'):
                    doc = CandidatosDocumentos.objects.create(check_proveedor='Y', candidatos=candidato, documentos_id=documento)
                    doc.save()

            if Candidatos.objects.filter(solicitudes_vacantes_id=candidato.solicitudes_vacantes_id).count()==1:
                SolicitudesEstatus.objects.filter(solicitudes_vacantes_id=candidato.solicitudes_vacantes_id).update(activo='N')
                estatus = Estatus.objects.get(tipos='solicitud', estatus='En proceso')
                solicitud_estatus = SolicitudesEstatus.objects.create(
                    solicitudes_vacantes_id=candidato.solicitudes_vacantes_id,
                    estatus=estatus)
                solicitud_estatus.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class CandidatosUpdate(UpdateView):
    """ Vista que permite actualizar los datos del candidatos """
    model = Candidatos
    second_model = Personas
    template_name = "solicitudes/create_candidatos.html"
    form_class = CandidatosForm
    second_form_class = PersonasForm


    #@login_required(login_url="Log_In")
    def get_context_data(self, **kwargs) :
        context = super(CandidatosUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        candidato = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=candidato.personas_id)

        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Editar Candidato.'}
        context['solicitudes_id'] = candidato.solicitudes_vacantes_id
        context['documentos'] = Documentos.objects.raw("""SELECT d.*, cd.check_proveedor FROM documentos d
LEFT JOIN candidatos_documentos cd ON cd.documentos_id=d.id AND cd.candidatos_id=%s
WHERE d.activo='Y' """,(pk,))

        if 'form' not in context:
            context['form'] = self.form_class(instance=candidato)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance=persona)

        return context

    #@login_required(login_url="Log_In")
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        candidato_id = kwargs['pk']
        candidato = self.model.objects.get(id=candidato_id)
        persona = self.second_model.objects.get(id=candidato.personas_id)

        form = self.form_class(request.POST, request.FILES, instance=candidato)
        form2 = self.second_form_class(request.POST, request.FILES, instance=persona)

        if form.is_valid() and form2.is_valid():

            candidato = form.save()
            form2.save()
            
            if request.POST.getlist('documentos[]'):
                CandidatosDocumentos.objects.filter(candidatos=candidato).update(check_proveedor='N')
                for documento in request.POST.getlist('documentos[]'):
                    
                    if CandidatosDocumentos.objects.filter(candidatos=candidato, documentos_id=documento).exists():
                        CandidatosDocumentos.objects.filter(candidatos=candidato, documentos_id=documento).update(check_proveedor='Y')
                    else:
                        doc = CandidatosDocumentos.objects.create(check_proveedor='Y', candidatos=candidato, documentos_id=documento)
                        doc.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))



def createRechazo(request, candidatos_id):
    """Vista que permite cambiar a rechazado un candidato"""
    titles = {"title_page":'Solicitudes',"sub_title_page":'Rechazo del candidato.'}
    
    if request.method == "POST":
        formulario = EstatusCandidatosForm(request.POST or None)
        if formulario.is_valid():
            
            CandidatosEstatus.objects.filter(candidatos_id=candidatos_id).update(activo='N')
            candidato = Candidatos.objects.get(id=candidatos_id)

            candidatoestatus = formulario.save(commit=False)
            candidatoestatus.candidatos = candidato
            candidatoestatus.estatus = Estatus.objects.get(tipos='candidato',estatus='Rechazado')

            candidatoestatus.save()
            return redirect('DetailsSolicitudes', id=candidato.solicitudes_vacantes_id)
        else:
            return redirect('Home')
    formulario = EstatusCandidatosForm()    

    return render(request,"solicitudes/create_rechazo.html",{"titles":titles, "formulario":formulario,"candidatos_id":candidatos_id})


""" Gestion de entrevistas """

@login_required(login_url="Log_In")
def entrevistasView(request, tipo_evento):
    """Vista que muestra las entrevistas pendientes"""
    
    titles = {"title_page":'Agenda',"sub_title_page":'Gestión de entrevistas.'}
    hoy = datetime.date.today()
    
    if request.method == "POST":
        formulario = AgendaForm(request.POST or None)
        
        if formulario.is_valid():
            entrevistas = Entrevistas.objects.filter(asistio__isnull='True', tipo_evento=request.POST['tipo_evento'])
            return render(request,"solicitudes/entrevistas.html",{"titles":titles, "entrevistas":entrevistas, "formulario":formulario})

    formulario = AgendaForm()
    entrevistas = Entrevistas.objects.filter(asistio__isnull='True', tipo_evento=tipo_evento)

    return render(request,"solicitudes/entrevistas.html",{"titles":titles, "entrevistas":entrevistas, "formulario":formulario,"hoy":hoy})



@login_required(login_url="Log_In")
def createEntrevistas(request, candidatos_id):
    """Vista que permite agendar entrevistas de los candidatos"""

    titles = {"title_page":'Reclutamiento',"sub_title_page":'Agendar nueva entrevista.'}
    if request.method == "POST":
        formulario = EntrevistasForm(request.POST or None)
        candidato = Candidatos.objects.get(id=candidatos_id)
        if formulario.is_valid():
            entrevista = formulario.save(commit=False)
            entrevista.candidatos = candidato
            entrevista.save()
            
            CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
            estatus = Estatus.objects.get(tipos='candidato', estatus='Programado')
            ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
            ce.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidatos_id":candidatos_id})
    
    candidato = Candidatos.objects.get(id=candidatos_id)
    formulario = EntrevistasForm()
       
    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})


@login_required(login_url="Log_In")
def viewEntrevista(request, candidatos_id):
    """Esta vista permite ver al proveedor la cita de los candidatos"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la entrevista.'}
    candidato = Candidatos.objects.get(id=candidatos_id)
    entrevista = Entrevistas.objects.get(Q(candidatos_id=candidatos_id), Q(tipo_evento='entrevista'), (Q(asistio__isnull='True') | Q(asistio='Y')))
    if request.method == "POST":
        formulario = Entrevistas2Form(request.POST or None, instance=entrevista)
        if formulario.is_valid():
            ingreso = formulario.save(commit=False)
            if ingreso.fecha_entrevista is None:
                ingreso.fecha_entrevista = timezone.now()
            ingreso.save()
           
            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id)
    else:
        formulario = Entrevistas2Form(instance=entrevista)

    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})



class EntrevistasUpdate(UpdateView):
    """ Vista que permite actualizar los datos del candidatos """
    
    model = Candidatos
    second_model = Personas
    third_model = Entrevistas
    template_name = "solicitudes/edit_entrevista.html"
    
    form_class = CandidatosForm
    second_form_class = PersonasForm
    third_form_class = Entrevistas2Form

    def get_context_data(self, **kwargs) :
        context = super(EntrevistasUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        candidato = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='entrevista'), (Q(asistio__isnull='True') | Q(asistio='Y')))
        #entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), (Q(asistio__isnull='True') | Q(asistio='Y')))

        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Editar Candidato.'}
        context['solicitudes_id'] = candidato.solicitudes_vacantes_id
        context['documentos'] = Documentos.objects.raw("""SELECT d.*, cd.check_proveedor, cd.check_locacion FROM documentos d
LEFT JOIN candidatos_documentos cd ON cd.documentos_id=d.id AND cd.candidatos_id=%s
WHERE d.activo='Y' """,(pk,))


        if 'form' not in context:
            context['form'] = self.form_class(instance=candidato)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance=persona)
        if 'form3' not in context:
            context['form3'] =self.third_form_class(instance=entrevista)
        
        context['candidato'] = candidato

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        candidato_id = kwargs['pk']

        candidato = self.model.objects.get(id=candidato_id)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='entrevista'), (Q(asistio__isnull='True') | Q(asistio='Y')))
        #entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), (Q(asistio__isnull='True') | Q(asistio='Y')))

        form = self.form_class(request.POST, request.FILES, instance=candidato)
        form2 = self.second_form_class(request.POST, request.FILES, instance=persona)
        form3 = self.third_form_class(request.POST, request.FILES, instance=entrevista)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid():

            candidato = form.save()
            form2.save()
            
            entrevista = form3.save(commit=False)
            if entrevista.fecha_entrevista is None:
                entrevista.fecha_entrevista = timezone.now()
            entrevista.save()

            #Se procesan los documentos del candidato    
            if request.POST.getlist('documentos[]'):
                CandidatosDocumentos.objects.filter(candidatos=candidato).update(check_locacion='N')
                for documento in request.POST.getlist('documentos[]'):
                    
                    if CandidatosDocumentos.objects.filter(candidatos=candidato, documentos_id=documento).exists():
                        CandidatosDocumentos.objects.filter(candidatos=candidato, documentos_id=documento).update(check_locacion='Y')
                    else:
                        doc = CandidatosDocumentos.objects.create(check_locacion='Y', candidatos=candidato, documentos_id=documento)
                        doc.save()
                        
            #Se procesa el estus
            if entrevista.asistio == 'Y':
                CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Entrevistado')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
                ce.save()
            else:
                CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Postulado')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
                ce.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
            #return redirect('Entrevistas')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


#Gestion de entrevistas para contratación

@login_required(login_url="Log_In")
def createContratacion(request, candidatos_id):
    """Vista que permite agendar entrevistas para firmar contrato"""

    titles = {"title_page":'Reclutamiento',"sub_title_page":'Agendar nueva contratación.'}
    if request.method == "POST":
        formulario = EntrevistasForm(request.POST or None)
        candidato = Candidatos.objects.get(id=candidatos_id)
        if formulario.is_valid():
            entrevista = formulario.save(commit=False)
            entrevista.candidatos = candidato
            entrevista.tipo_evento = 'contratacion'
            entrevista.save()
            
            CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
            estatus = Estatus.objects.get(tipos='candidato', estatus='Contratación')
            ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
            ce.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidatos_id":candidatos_id})
    
    candidato = Candidatos.objects.get(id=candidatos_id)
    formulario = EntrevistasForm()
       
    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})



@login_required(login_url="Log_In")
def viewContratacion(request, candidatos_id):
    """Esta vista permite ver al proveedor la cita de los candidatos"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Información de la contratación.'}
    candidato = Candidatos.objects.get(id=candidatos_id)
    entrevista = Entrevistas.objects.get(Q(candidatos_id=candidatos_id), Q(tipo_evento='contratacion'), (Q(asistio__isnull='True') | Q(asistio='Y')))
    if request.method == "POST":
        formulario = Entrevistas3Form(request.POST or None, instance=entrevista)
        if formulario.is_valid():
            contratacion = formulario.save(commit=False)
            if contratacion.fecha_entrevista is None:
                contratacion.fecha_entrevista = timezone.now()
            contratacion.save()
           
            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id)
    else:
        formulario = Entrevistas3Form(instance=entrevista)

    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})



class ContratacionUpdate(UpdateView):
    """ Vista que permite actualizar los datos del candidatos """
    
    model = Candidatos
    second_model = Personas
    third_model = Entrevistas
    template_name = "solicitudes/edit_entrevista.html"
    
    form_class = CandidatosForm
    second_form_class = PersonasForm
    third_form_class = Entrevistas2Form
    fourth_form_class = Entrevistas3Form

    def get_context_data(self, **kwargs) :
        context = super(ContratacionUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        candidato = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='entrevista'), (Q(asistio__isnull='True') | Q(asistio='Y')))
        contratacion = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='contratacion'), (Q(asistio__isnull='True') | Q(asistio='Y')))

        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'información del Candidato.'}
        context['solicitudes_id'] = candidato.solicitudes_vacantes_id
        context['documentos'] = Documentos.objects.raw("""SELECT d.*, cd.check_proveedor, cd.check_locacion FROM documentos d
LEFT JOIN candidatos_documentos cd ON cd.documentos_id=d.id AND cd.candidatos_id=%s
WHERE d.activo='Y' """,(pk,))

        if 'form' not in context:
            context['form'] = self.form_class(instance=candidato)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=entrevista)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(instance=contratacion)
        
        context['candidato'] = candidato

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        candidato_id = kwargs['pk']

        candidato = self.model.objects.get(id=candidato_id)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='entrevista'), (Q(asistio__isnull='True') | Q(asistio='Y')))
        contratacion = self.third_model.objects.get(Q(candidatos_id=candidato.id), Q(tipo_evento='contratacion'), (Q(asistio__isnull='True') | Q(asistio='Y')))

        form = self.form_class(request.POST, request.FILES, instance=candidato)
        form2 = self.second_form_class(request.POST, request.FILES, instance=persona)
        form3 = self.third_form_class(request.POST, request.FILES, instance=entrevista)
        form4 = self.third_form_class(request.POST, request.FILES, instance=contratacion)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form3.is_valid():

            contratacion = form4.save(commit=False)
            if contratacion.fecha_entrevista is None:
                contratacion.fecha_entrevista = timezone.now()
            contratacion.save()
                        
            #Se procesa el estus
            if contratacion.asistio == 'Y':
                CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Contratado')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
                ce.save()
            else:
                CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
                CandidatosEstatus.objects.filter(candidatos_id=candidato.id, estatus='Entrevistado').update(activo='Y')
                """estatus = Estatus.objects.get(tipos='candidato', estatus='Postulado')
                ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id)
                ce.save()"""
            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


#Gestion de entrevistas para contratación

@login_required(login_url="Log_In")
def createIngreso(request, candidatos_id):
    """Vista que permite agendar el primer dia laboral"""

    titles = {"title_page":'Reclutamiento',"sub_title_page":'Agendar el primer día laboral.'}
    if request.method == "POST":
        formulario = EntrevistasForm(request.POST or None)
        candidato = Candidatos.objects.get(id=candidatos_id)
        if formulario.is_valid():
            entrevista = formulario.save(commit=False)
            entrevista.candidatos = candidato
            entrevista.tipo_evento = 'ingreso'
            entrevista.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidatos_id":candidatos_id})
    
    candidato = Candidatos.objects.get(id=candidatos_id)
    formulario = EntrevistasForm()
       
    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})


@login_required(login_url="Log_In")
def editIngreso(request, candidatos_id):
    """Esta vista permite confirmar la asistencia al primer dia laboral de un candidato contratado"""

    titles = {"title_page":'Solicitudes',"sub_title_page":'Confirmación de asistencia al dia laboral.'}
    candidato = Candidatos.objects.get(id=candidatos_id)
    entrevista = Entrevistas.objects.get(Q(candidatos_id=candidatos_id), Q(tipo_evento='ingreso'), (Q(asistio__isnull='True') | Q(asistio='Y')))
    if request.method == "POST":
        formulario = IngresoForm(request.POST or None, instance=entrevista)
        if formulario.is_valid():
            ingreso = formulario.save(commit=False)
            if ingreso.fecha_entrevista is None:
                ingreso.fecha_entrevista = timezone.now()
            ingreso.save()
           
            #CandidatosEstatus.objects.filter(candidatos_id=candidato.id).update(activo='N')
            estatus = Estatus.objects.get(tipos='candidato', estatus='Ingreso')
            ce = CandidatosEstatus.objects.create(candidatos_id=candidato.id, estatus_id=estatus.id, activo='N')
            ce.save()

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id)
    else:
        formulario = IngresoForm(instance=entrevista)

    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})



def staffAutorizado(request, locaciones_id, puestos_operativos_id):
    """vista que devuelve json de los puestos de una locación"""
    #if request.method == 'POST':
    puesto = serialize('json',LocacionesPuestos.objects.filter(locaciones_id=locaciones_id,puestos_operativos_id=puestos_operativos_id,activo='Y'))
    return HttpResponse(puesto, 'application/json')