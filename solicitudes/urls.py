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

    path('create_candidatos/<int:solicitudes_id>',views.CandidatosCreate.as_view(), name="CreateCandidatos"),
    path('edit_candidatos/<int:pk>',views.CandidatosUpdate.as_view(), name="EditCandidatos"),

    path('entrevistas',views.entrevistasView, name="Entrevistas"),
    
    path('create_entrevistas/<int:candidatos_id>',views.createEntrevistas, name="CreateEntrevistas"),
    path('view_entrevistas/<int:candidatos_id>',views.viewEntrevista, name="ViewEntrevistas"),
    path('edit_entrevistas/<int:pk>',views.EntrevistasUpdate.as_view(), name="EditEntrevistas"),

    path('create_contratacion/<int:candidatos_id>',views.createContratacion, name="CreateContratacion"),
    path('view_contratacion/<int:candidatos_id>',views.viewContratacion, name="ViewContratacion"),
    path('edit_contratacion/<int:pk>',views.ContratacionUpdate.as_view(), name="EditContratacion"),

    path('create_ingreso/<int:candidatos_id>',views.createIngreso, name="CreateIngreso"),
    path('edit_ingreso/<int:candidatos_id>',views.editIngreso, name="EditIngreso"),

    path('rechazo_candidato/<int:candidatos_id>',views.createRechazo, name="RechazoCandidato"),
    
    path('staff_autorizado/<int:locaciones_id>/<int:puestos_operativos_id>',views.staffAutorizado, name="StaffAutorizado"),
]