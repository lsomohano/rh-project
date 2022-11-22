from django.urls import path
from . import views

urlpatterns = [
    path('',views.facturasView, name="Facturacion"),
    path('create_facturacion/',views.createFacturacion, name="CreateFacturacion"),
    #path('edit_solicitudes/<int:id>',views.editSolicitudes, name="EditSolicitudes"),
    path('details_facturacion/<int:id>',views.detailsFacturacion, name="DetailsFacturacion"),
    path('add_prefactura/<int:id>',views.addPrefactura, name="AddPrefactura"),
    path('add_factura/<int:id>',views.addFactura, name="AddFactura"),
    path('payment_factura/<int:id>',views.paymentFactura, name="PaymentFactura"),

    path('add_candidatos/<int:proveedores_id>/<int:facturas_id>/<fecha_ini>/<fecha_fin>',views.addCandidatos, name="AddCandidatos"),
    #path('candidatos_list/<int:facturas_id>/<fecha_ini>/<fecha_fin>',views.listCandidatosJson, name="ListCandidatos"),
]
