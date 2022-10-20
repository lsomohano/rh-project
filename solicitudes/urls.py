from django.urls import path
from . import views

urlpatterns = [
    path('',views.solicitudesView, name="Solicitudes"),
    path('create_solicitudes/',views.createSolicitudes, name="CreateSolicitudes"),
    path('edit_solicitudes/<int:id>',views.editSolicitudes, name="EditSolicitudes"),
    path('details_solicitudes/<int:id>',views.detailsSolicitudes, name="DetailsSolicitudes"),
    #path('create_candidatos/<int:solicitudes_id>',views.createCandidatos, name="CreateCandidatos"),
    path('estatus',views.estatusView, name="Estatus"),
    path('create_estatus/',views.createEstatus, name="CreateEstatus"),
    path('edit_estatus/<int:id>',views.editEstatus, name="EditEstatus"),

    path('create_candidatos/<int:solicitudes_id>',views.CandidatosCreate.as_view(), name="CreateCandidatos")
]