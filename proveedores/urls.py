from django.urls import path
from . import views

urlpatterns = [
    path('',views.proveedores, name="Proveedores"),
    path('create_proveedores/',views.createView, name="CreateProveedores"),
    path('edit_proveedores/<int:id>',views.editView, name="EditProveedores"),
    path('details/<int:id>',views.detailsView, name="Details"),
    path('delete_proveedores/<int:id>',views.deleteView, name="DeleteProveedores"),

    path('create_contacto/<int:proveedores_id>',views.createContactosView, name="CreateContacto"),
    path('edit_contacto/<int:id>',views.editContactosView, name="EditContacto"),
    path('delete_contacto/<int:id>',views.DeleteContactosView, name="DeleteContacto"),

    path('create_locacion/<int:proveedores_id>',views.createLocacionesViews, name="CreateLocacion"),
    path('delete_locacion/<int:id>',views.DeleteLocacionesView, name="DeleteLocacion"),
]