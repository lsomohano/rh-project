from django.urls import path
from .views import RegistroUsuarios, log_out, log_in

urlpatterns = [
    path('',RegistroUsuarios.as_view(), name="Autenticacion"),
    path('log_out',log_out, name="Log_Out"),
    path('log_in',log_in, name="Log_In"),
]