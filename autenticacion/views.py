from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

def log_out(request):
    logout(request)
    return redirect("/")

def log_in(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasena)

            if usuario is not None:
                login(request, usuario)
                return redirect("/")
            else:
                messages.error(request, "Usuario o Contraseña Incorecta.")
        else:
            messages.error(request, "Usuario o Contraseña Incorecta.")

    form= AuthenticationForm()
    return render(request, "autenticacion/login.html",{"form":form})


"""def autenticacion(request):
    titles = {"title_page":'Autenticación',"sub_title_page":'Página de gestión de usuarios.'}
    return render(request, "autenticacion/registro.html",{"titles":titles})"""