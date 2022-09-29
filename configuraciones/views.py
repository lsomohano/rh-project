from django.shortcuts import render, redirect
from .models import Entidades
from .forms import entidadesCreate
# Create your views here.

def EntidadesView(request):
    titles = {"title_page":'Entidades',"sub_title_page":'Gestión de info de Entidades.'}
    entidades = Entidades.objects.filter(activo='Y')
    return render(request,"configuraciones/entidades.html",{"titles":titles, "entidades":entidades})

def createEntidades(request):
    titles = {"title_page":'Entidades',"sub_title_page":'Nueva entidad.'}
    if request.method == "POST":
        formulario = entidadesCreate(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entidades')
    
    formulario = entidadesCreate()
       
    return render(request,"configuraciones/create.html",{"titles":titles, "formulario":formulario})