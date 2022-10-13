from django.urls import path
from . import views

urlpatterns = [
    path('',views.solicitudesView, name="Solicitudes"),
    path('create_solicitudes/',views.createSolicitudes, name="CreateSolicitudes"),
    path('details_solicitudes/<int:id>',views.detailsSolicitudes, name="DetailsSolicitudes")
]