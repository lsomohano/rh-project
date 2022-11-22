from django.shortcuts import render, redirect
from .models import Ciudades, Contactos, Entidades, PuestosNominas, PuestosOperativos, Locaciones, LocacionesPuestos
from .forms import ContactosLocacionesCreation, PuestosLocacionesCreation, ciudadesCreate, entidadesCreate, puestosNominasCreate, puestosOperativosCreate, LocacionesCreate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="Log_In")
def entidadesView(request):
    """Vista que gestiona la información de las entidades"""
    titles = {"title_page":'Entidades',"sub_title_page":'Gestión de info de Entidades.'}
    entidades = Entidades.objects.filter(activo='Y')
    return render(request,"configuraciones/entidades.html",{"titles":titles, "entidades":entidades})


@login_required(login_url="Log_In")
def createEntidades(request):
    """Vista que permite agregar nuevas entidades"""
    titles = {"title_page":'Entidades',"sub_title_page":'Nueva entidad.'}
    if request.method == "POST":
        formulario = entidadesCreate(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entidades')
    
    formulario = entidadesCreate()
       
    return render(request,"configuraciones/create.html",{"titles":titles, "formulario":formulario})

@login_required(login_url="Log_In")
def editEntidades(request, id):
    """Vista que permite editar la información una entidad"""
    titles = {"title_page":'Entidades',"sub_title_page":'Editar información de la entidad.'}
    entidades = Entidades.objects.get(id=id)
    if request.method == "POST":
        formulario = entidadesCreate(request.POST or None, instance=entidades)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entidades')
    else:
        formulario = entidadesCreate(instance=entidades)

    return render(request,"configuraciones/edit.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def ciudadesView(request):
    titles = {"title_page":'Ciudades',"sub_title_page":'Gestión de info de ciudades.'}
    ciudades = Ciudades.objects.filter(activo='Y')
    return render(request,"configuraciones/ciudades.html",{"titles":titles, "ciudades":ciudades})


@login_required(login_url="Log_In")
def createCiudades(request):
    titles = {"title_page":'Entidades',"sub_title_page":'Nueva entidad.'}
    if request.method == "POST":
        formulario = ciudadesCreate(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Ciudades')
    
    formulario = ciudadesCreate()
       
    return render(request,"configuraciones/create.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def editCiudades(request, id):

    titles = {"title_page":'Proveedores',"sub_title_page":'Editar información de ciudad.'}
    ciudad = Ciudades.objects.get(id=id)
    if request.method == "POST":
        formulario = ciudadesCreate(request.POST or None, instance=ciudad)
        if formulario.is_valid():
            formulario.save()
            return redirect('Ciudades')
    else:
        formulario = ciudadesCreate(instance=ciudad)

    return render(request,"configuraciones/edit.html",{"titles":titles, "formulario":formulario, "id":id})


""" --- Gestion de Puesto Nomina --- """

@login_required(login_url="Log_In")
def puestosView(request):
    titles = {"title_page":'Puestos de Nomina',"sub_title_page":'Gestión de los puestos de trabajo.'}
    puestos = PuestosNominas.objects.filter(activo='Y')
    return render(request,"configuraciones/puestos.html",{"titles":titles, "puestos":puestos})


@login_required(login_url="Log_In")
def createPuestoNomina(request):
    titles = {"title_page":'Puestos Nomina',"sub_title_page":'Nuevo puesto nomina.'}
    if request.method == "POST":
        formulario = puestosNominasCreate(request.POST or None)
        if formulario.is_valid():
            puesto = formulario.save()
            return redirect('DetailsPuestos',id=puesto.id)
    
    formulario = puestosNominasCreate()
       
    return render(request,"configuraciones/create.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def editPuestosNominas(request, id):

    titles = {"title_page":'Puestos nominas',"sub_title_page":'Editar información del puesto.'}
    puesto = PuestosNominas.objects.get(id=id)
    if request.method == "POST":
        formulario = puestosNominasCreate(request.POST or None, instance=puesto)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsPuestos',id=id)
    else:
        formulario = puestosNominasCreate(instance=puesto)

    return render(request,"configuraciones/edit.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def deletePuestosNominas(request, id):

    puesto = PuestosNominas.objects.get(id=id)
    puesto.activo='N'
    puesto.save()

    return redirect('Puestos')


@login_required(login_url="Log_In")
def detailsPuestos(request, id):
    
    titles = {"title_page":'Puestos nominas',"sub_title_page":'Información del proveedor.'}
    puesto = PuestosNominas.objects.get(id=id)
    puestos_operativos = PuestosOperativos.objects.filter(puestos_nominas_id=id, activo='Y')

    return render(request,"configuraciones/details_puestos.html",{
        "titles":titles, 
        "puesto":puesto, 
        "puestos_operativos":puestos_operativos})


""" --- Gestion de Puesto Operativos --- """

@login_required(login_url="Log_In")
def createPuestoOperativo(request,puestos_nominas_id):
    titles = {"title_page":'Puestos Operativo',"sub_title_page":'Nuevo puesto operativo.'}
    if request.method == "POST":
        formulario = puestosOperativosCreate(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsPuestos',id=puestos_nominas_id)
    
    formulario = puestosOperativosCreate()
       
    return render(request,"configuraciones/create_po.html",{"titles":titles, "formulario":formulario,"puestos_nominas_id":puestos_nominas_id})


@login_required(login_url="Log_In")
def editPuestosOperativos(request, id):

    titles = {"title_page":'Puestos nominas',"sub_title_page":'Editar información del puesto.'}
    puesto = PuestosOperativos.objects.get(id=id)
    if request.method == "POST":
        formulario = puestosOperativosCreate(request.POST or None, instance=puesto)
        if formulario.is_valid():
            puestos_nominas_id = formulario['puestos_nominas'].value()
            formulario.save()
            return redirect('DetailsPuestos',id=puestos_nominas_id)
    else:
        formulario = puestosOperativosCreate(instance=puesto)

    return render(request,"configuraciones/edit_po.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def deletePuestosOperativos(request, id):

    puesto = PuestosOperativos.objects.get(id=id)
    puestos_nominas_id = puesto.puestos_nominas_id
    puesto.activo='N'
    puesto.save()

    return redirect('DetailsPuestos',id=puestos_nominas_id)


""" --- Gestion de locaciones --- """

@login_required(login_url="Log_In")
def locacionesView(request):
    titles = {"title_page":'Locaciones',"sub_title_page":'Gestión de las locaciones.'}
    locaciones = Locaciones.objects.filter(activo='Y')
    return render(request,"configuraciones/locaciones.html",{"titles":titles, "locaciones":locaciones})


@login_required(login_url="Log_In")
def createLocaciones(request):
    titles = {"title_page":'Locaciones',"sub_title_page":'Nuevo puesto nomina.'}
    if request.method == "POST":
        formulario = LocacionesCreate(request.POST or None, request.FILES)
        if formulario.is_valid():
            locacion = formulario.save()
            return redirect('DetailsLocaciones',id=locacion.id)
    
    formulario = LocacionesCreate()
       
    return render(request,"configuraciones/create.html",{"titles":titles, "formulario":formulario})


@login_required(login_url="Log_In")
def editLocaciones(request, id):

    titles = {"title_page":'Locaciones',"sub_title_page":'Editar información de la locación.'}
    locacion = Locaciones.objects.get(id=id)
    if request.method == "POST":
        formulario = LocacionesCreate(request.POST or None, request.FILES, instance=locacion)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsLocaciones',id=id)
    else:
        formulario = LocacionesCreate(instance=locacion)

    return render(request,"configuraciones/edit.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def detailsLocaciones(request, id):
    
    titles = {"title_page":'Locaciones',"sub_title_page":'Información de la locación.'}
    locacion = Locaciones.objects.get(id=id)
    contactos = Contactos.objects.filter(locaciones_id=id, activo='Y')
    puestos = LocacionesPuestos.objects.filter(locaciones_id=id, activo='Y')

    return render(request,"configuraciones/details_locaciones.html",{
        "titles":titles, 
        "locacion":locacion, 
        "contactos":contactos, 
        "puestos":puestos})


""" Modulo de contactos de las locaciones"""

@login_required(login_url="Log_In")
def createContacto(request, locaciones_id):
    titles = {"title_page":'Locaciones',"sub_title_page":'Nuevo contacto.'}
    if request.method == "POST":
        formulario = ContactosLocacionesCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsLocaciones', id=locaciones_id)
    
    formulario = ContactosLocacionesCreation()
       
    return render(request,"configuraciones/create_contactos.html",{"titles":titles, "formulario":formulario,"locaciones_id":locaciones_id})


@login_required(login_url="Log_In")
def editContacto(request, id):

    titles = {"title_page":'Locaciones',"sub_title_page":'Editar información del contacto.'}
    contacto = Contactos.objects.get(id=id)
    if request.method == "POST":
        formulario = ContactosLocacionesCreation(request.POST or None, instance=contacto)
        if formulario.is_valid():
            locaciones_id = formulario['locaciones'].value()
            formulario.save()
            return redirect('DetailsLocaciones',id=locaciones_id)
    else:
        formulario = ContactosLocacionesCreation(instance=contacto)

    return render(request,"configuraciones/edit_contactos.html",{"titles":titles, "formulario":formulario, "id":id})


@login_required(login_url="Log_In")
def deleteContacto(request, id):

    contacto = Contactos.objects.get(id=id)
    locaciones_id = contacto.locaciones_id
    contacto.activo='N'
    contacto.save()

    return redirect('DetailsLocaciones',id=locaciones_id)

""" Asignación de puestos a locaciones """

@login_required(login_url="Log_In")
def createLocacinesPuestos(request, locaciones_id):
    titles = {"title_page":'Locaciones',"sub_title_page":'Agregar puestos.'}
    if request.method == "POST":
        formulario = PuestosLocacionesCreation(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('DetailsLocaciones', id=locaciones_id)
    
    formulario = PuestosLocacionesCreation()
    return render(request,"configuraciones/create_contactos.html",{"titles":titles, "formulario":formulario,"locaciones_id":locaciones_id})


@login_required(login_url="Log_In")
def editLocacinesPuestos(request, id):

    titles = {"title_page":'Locaciones',"sub_title_page":'Editar información del puesto.'}
    puesto = LocacionesPuestos.objects.get(id=id)
    if request.method == "POST":
        formulario = PuestosLocacionesCreation(request.POST or None, instance=puesto)
        if formulario.is_valid():
            locaciones_id = formulario['locaciones'].value()
            formulario.save()
            return redirect('DetailsLocaciones',id=locaciones_id)
    else:
        formulario = PuestosLocacionesCreation(instance=puesto)

    return render(request,"configuraciones/edit_contactos.html",{"titles":titles, "formulario":formulario, "id":id})