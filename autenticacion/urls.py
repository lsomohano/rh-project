from django.urls import path
from .views import RegistroUsuarios

urlpatterns = [
    path('',RegistroUsuarios.as_view(), name="Autenticacion"),
    
]