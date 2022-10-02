from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserCreationForm
# Create your views here.

class RegistroUsuarios(View):
    def get(self, request):
        formulario = UserCreationForm()
        titles = {"title_page":'Autenticación',"sub_title_page":'Página de gestión de usuarios.'}
        return render(request, "autenticacion/registro.html",{"titles":titles,"formulario":formulario})

    def post(self, request):
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('Home')
        else:
            titles = {"title_page":'Autenticación',"sub_title_page":'Página de gestión de usuarios.'}
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
            return render(request, "autenticacion/registro.html",{"titles":titles,"formulario":formulario})


"""def autenticacion(request):
    titles = {"title_page":'Autenticación',"sub_title_page":'Página de gestión de usuarios.'}
    return render(request, "autenticacion/registro.html",{"titles":titles})"""