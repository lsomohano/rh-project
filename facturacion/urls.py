from django.urls import path
from . import views

urlpatterns = [
    path('',views.facturasView, name="Facturacion"),
    path('create_facturacion/',views.createFacturacion, name="CreateFacturacion"),
    #path('edit_solicitudes/<int:id>',views.editSolicitudes, name="EditSolicitudes"),
    path('details_facturacion/<int:id>',views.detailsFacturacion, name="DetailsFacturacion"),

    path('add_candidatos/<fecha_ini>/<fecha_fin>',views.addCandidatos, name="AddCandidatos"),
    path('candidatos_list/<fecha_ini>/<fecha_fin>',views.listCandidatosJson, name="ListCandidatos"),
]
