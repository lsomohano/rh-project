from socket import create_server
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .models import Candidatos, Personas, SolicitudesVacantes, SolicitudesEstatus, Estatus, CandidatosEstatus
from configuraciones.models import Locaciones, PuestosOperativos
from .forms import CandidatosForm, PersonasForm, SolicitudesForm, EstatusForm


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

    candidatos = Candidatos.objects.filter(solicitudes_vacantes_id=id).prefetch_related('id__candidatos_estatus')
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


##### Gestion de las vacantes #####
class CandidatosCreate(CreateView):
    """Vista que permite agregar infomación de lo"""
    model = Candidatos
    template_name = "solicitudes/create_candidatos.html"
    form_class = CandidatosForm
    second_form_class = PersonasForm

    def get_context_data(self, **kwargs):
        context = super(CandidatosCreate, self).get_context_data(**kwargs)
        context['titles'] = {"title_page":'Candidatos',"sub_title_page":'Nuevo Candidato.'}
        context['solicitudes_id'] = self.kwargs.get('solicitudes_id')
        
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

            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class CandidatosUpdate(UpdateView):
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
        context['solicitudes_id'] = self.kwargs.get('solicitudes_id')
        
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
            
            return redirect('DetailsSolicitudes',id=candidato.solicitudes_vacantes_id) 
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))