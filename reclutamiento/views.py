from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from microsoft_authentication.auth.auth_decorators import microsoft_login_required

# Create your views here.

@login_required(login_url="Log_In")
def home(request):
    titles = {"title_page":'Dashboard',"sub_title_page":'Pagina principal.'}

    return render(request,"reclutamiento/home.html",{"titles":titles})