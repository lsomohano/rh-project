from django.shortcuts import render, HttpResponse
from django.views.generic import UpdateView, ListView, View
from .models import Proveedores, ContactosProveedores

# Create your views here.

def proveedores(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Gestión de info de Provedores.'}
    proveedores = Proveedores.objects.all()
    return render(request,"proveedores/proveedores.html",{"titles":titles, "proveedores":proveedores})


def create(request):
    titles = {"title_page":'Proveedores',"sub_title_page":'Gestión de info de Provedores.'}
    #proveedores = Proveedores.objects.all()
    return render(request,"proveedores/create.html",{"titles":titles})