from django.urls import path
from . import views

urlpatterns = [

    path('entidades/',views.EntidadesView, name="Entidades"),
    path('create_entidades/',views.createEntidades, name="CreateEntidades"),
    path('edit_entidades/<int:id>',views.editEntidades, name="EditEntidades"),

    path('entidades/',views.entidadesView, name="Entidades"),
    path('create/',views.createEntidades, name="Create"),

    path('ciudades/',views.ciudadesView, name="Ciudades"),
    path('create_ciudades/',views.createCiudades, name="CreateCiudades"),
    path('edit_ciudades/<int:id>',views.editCiudades, name="EditCiudades"),
    path('delete_ciudades/<int:id>',views.editCiudades, name="DeleteCiudades"),


    path('puestos/',views.puestosView, name="Puestos"),
    path('create_puestos/',views.createPuestoNomina, name="CreatePuestosNomina"),
    path('edit_puestos/<int:id>',views.editPuestosNominas, name="EditPuestosNomina"),
    path('details_puestos/<int:id>',views.detailsPuestos, name="DetailsPuestos"),
    path('delete_puestos/<int:id>',views.deletePuestosNominas, name="DeletePuestosNominas"),
    #path('edit/<int:id>',views.editView, name="Edit"),
    #path('details/<int:id>',views.detailsView, name="Details"),
    #path('delete/<int:id>',views.deleteView, name="Delete"),

    path('create_operativo/<int:puestos_nominas_id>',views.createPuestoOperativo, name="CreatePuestoOperativo"),
    path('edit_operativo/<int:id>',views.editPuestosOperativos, name="EditPuestoOperativo"),
    path('delete_operativo/<int:id>',views.deletePuestosOperativos, name="DeletePuestosOperativo"),
    #path('delete_contacto/<int:id>',views.DeleteContactosView, name="DeleteContacto"),

    #path('create_locacion/<int:proveedores_id>',views.createLocacionesViews, name="CreateLocacion"),
    #path('delete_locacion/<int:id>',views.DeleteLocacionesView, name="DeleteLocacion"),

    path('locaciones/',views.locacionesView, name="Locaciones"),
    path('create_locaciones/',views.createLocaciones, name="CreateLocaciones"),
    path('edit_locaciones/<int:id>',views.editLocaciones, name="EditLocaciones"),
    path('details_locaciones/<int:id>',views.detailsLocaciones, name="DetailsLocaciones"),
]