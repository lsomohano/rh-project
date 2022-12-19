from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from microsoft_authentication.auth.auth_decorators import microsoft_login_required

# Create your views here.

@login_required(login_url="Log_In")
def home(request):
    titles = {"title_page":'Dashboard',"sub_title_page":'Pagina principal.'}

    return render(request,"reclutamiento/home.html",{"titles":titles})


def error_404(request,exception):
    titles = {"title_page":'404',"sub_title_page":'Error Page.'}
    return render(request,"reclutamiento/error_404.html",{"titles":titles})

def error_500(request):
    titles = {"title_page":'500',"sub_title_page":'Internal Server Error.'}
    return render(request,"reclutamiento/error_500.html",{"titles":titles})