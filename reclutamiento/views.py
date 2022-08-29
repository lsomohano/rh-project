from turtle import title
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    titles = {"title_page":'Home',"sub_title_page":'Pagina principal.'}

    return render(request,"reclutamiento/home.html",{"titles":titles})