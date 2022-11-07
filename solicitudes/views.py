from socket import create_server
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .models import Candidatos, Entrevistas, Personas, SolicitudesVacantes, SolicitudesEstatus, Estatus, CandidatosEstatus, Documentos, CandidatosDocumentos
from configuraciones.models import Locaciones, PuestosOperativos, activo
from .forms import CandidatosForm, EntrevistasForm, PersonasForm, SolicitudesForm, EstatusForm, Entrevistas2Form
from django.db.models import Q

import datetime

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

    if request.user.id != 1:
        qs = Locaciones.objects.filter(contactos__user_id=request.user.id).select_related()
        formulario.fields['locaciones'].queryset = qs
        formulario.fields['puestos_operativos'].queryset = PuestosOperativos.objects.filter(locacionespuestos__locaciones__contactos__user_id=2)

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

    #candidatos = Candidatos.objects.filter(solicitudes_vacantes_id=id).select_related('personas').prefetch_related('id__candidatos_estatus')
    candidatos = Candidatos.objects.raw("""SELECT c.id, c.created, c.aceptado, c.personas_id, p.nombre, p.apellido_paterno,p.apellido_materno, p.rfc, p.fecha_nacimiento, p.email, p.genero, ce.created AS fecha_estatus, e.estatus, e.descripcion FROM candidatos c
                                            INNER JOIN personas p ON p.id=c.personas_id
                                            INNER JOIN candidatos_estatus ce ON ce.candidatos_id=c.id AND ce.activo='Y'
                                            INNER JOIN calogos_estatus e ON e.id=ce.estatus_id
                                            WHERE c.solicitudes_vacantes_id=%s""",(id,))
                                                

    return render(request,"solicitudes/details_solicitud.html",{
        "titles":titles, 
        "solicitud":solicitud, 
        "estatus":estatus,
        "candidatos":candidatos,
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


##### Gestion de los candidatos #####
class CandidatosCreate(CreateView):
    """ Vista que permite agregar infomación de los candidatos """
    model = Candidatos
    template_name = "solicitudes/create_candidatos.html"
    form_class = CandidatosForm
    second_form_class = PersonasForm

    def get_context_data(self, **kwargs):
        context = super(CandidatosCreate, self).get_context_data(**kwargs)
        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Nuevo Candidato.'}
        context['solicitudes_id'] = self.kwargs.get('solicitudes_id')
        context['documentos'] = Documentos.objects.filter(activo='Y')

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(self.request.GET)

        return context
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            candidato = form.save(commit=False)
            candidato.personas = form2.save()
            candidato.save()

            #Se asigna un estatus al candidato
            estatus = Estatus.objects.get(tipos='candidato', estatus='En proceso')
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
        #context['candidatosdocumentos'] = CandidatosDocumentos.objects.filter(candidatos_id=pk)

        if 'form' not in context:
            context['form'] = self.form_class(instance=candidato)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance=persona)

        return context

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


""" Gestion de entrevistas """

def entrevistasView(request):
    """Vista que muestra las entrevistas pendientes"""
    
    titles = {"title_page":'Entrevistas',"sub_title_page":'Gestión de entrevistas.'}
    entrevistas = Entrevistas.objects.filter(asistio__isnull='True')
    hoy = datetime.datetime.now().date()

    return render(request,"solicitudes/entrevistas.html",{"titles":titles, "entrevistas":entrevistas, "hoy":hoy})



def createEntrevistas(request, candidatos_id):
    """Vista que permite agendar entrevistas de los candidatos"""

    titles = {"title_page":'Reclutamiento',"sub_title_page":'Agendar nueva entrevista.'}
    if request.method == "POST":
        formulario = EntrevistasForm(request.POST or None)
        if formulario.is_valid():
            entrevista = formulario.save(commit=False)
            entrevista.candidatos = Candidatos.objects.get(id=candidatos_id)
            entrevista.save()
            return redirect('Estatus')
        else:
            return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidatos_id":candidatos_id})
    
    candidato = Candidatos.objects.get(id=candidatos_id)
    formulario = EntrevistasForm()
       
    return render(request,"solicitudes/create_entrevistas.html",{"titles":titles, "formulario":formulario, "candidato":candidato})


class EntrevistasUpdate(UpdateView):
    """ Vista que permite actualizar los datos del candidatos """
    
    model = Candidatos
    second_model = Personas
    third_model = Entrevistas
    template_name = "solicitudes/create_candidatos.html"
    
    form_class = CandidatosForm
    second_form_class = PersonasForm
    third_form_class = Entrevistas2Form

    def get_context_data(self, **kwargs) :
        context = super(EntrevistasUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        candidato = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(candidatos_id=candidato.id, asistio__isnull='True')

        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Editar Candidato.'}
        context['solicitudes_id'] = candidato.solicitudes_vacantes_id
        context['documentos'] = Documentos.objects.raw("""SELECT d.*, cd.check_proveedor FROM documentos d
LEFT JOIN candidatos_documentos cd ON cd.documentos_id=d.id AND cd.candidatos_id=%s
WHERE d.activo='Y' """,(pk,))
        #context['candidatosdocumentos'] = CandidatosDocumentos.objects.filter(candidatos_id=pk)

        if 'form' not in context:
            context['form'] = self.form_class(instance=candidato)
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance=persona)
        if 'form3' not in context:
            context['form3'] =self.third_form_class(instance=entrevista)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        candidato_id = kwargs['pk']

        candidato = self.model.objects.get(id=candidato_id)
        persona = self.second_model.objects.get(id=candidato.personas_id)
        entrevista = self.third_model.objects.get(candidatos_id=candidato.id, asistio__isnull='True')

        form = self.form_class(request.POST, request.FILES, instance=candidato)
        form2 = self.second_form_class(request.POST, request.FILES, instance=persona)
        form3 = self.third_form_class(request.POST, request.FILES, instance=entrevista)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid():

            candidato = form.save()
            form2.save()
            form3.save()

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
            if form3.asistio == 'Y':
                CandidatosEstatus.objects.filter(candidato_id=candidato.id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Entrevistado')
                ce = CandidatosEstatus.objects.create(candidato_id=candidato.id, estatus_id=estatus.id)
                ce.save()
            else:
                CandidatosEstatus.objects.filter(candidato_id=candidato.id).update(activo='N')
                estatus = Estatus.objects.get(tipos='candidato', estatus='Postulado')
                ce = CandidatosEstatus.objects.create(candidato_id=candidato.id, estatus_id=estatus.id)
                ce.save()

            #return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
            return redirect('Entrevistas')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))