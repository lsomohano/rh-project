from django.urls import path
from . import views

urlpatterns = [
    path('entidades/',views.EntidadesView, name="Entidades"),
    path('create_entidades/',views.createEntidades, name="CreateEntidades"),
    path('edit_entidades/<int:id>',views.editEntidades, name="EditEntidades"),
    #path('details/<int:id>',views.detailsView, name="Details"),
    #path('delete/<int:id>',views.deleteView, name="Delete"),

    #path('create_contacto/<int:proveedores_id>',views.createContactosView, name="CreateContacto"),
    #path('edit_contacto/<int:id>',views.editContactosView, name="EditContacto"),
    #path('delete_contacto/<int:id>',views.DeleteContactosView, name="DeleteContacto"),

    #path('create_locacion/<int:proveedores_id>',views.createLocacionesViews, name="CreateLocacion"),
    #path('delete_locacion/<int:id>',views.DeleteLocacionesView, name="DeleteLocacion"),
]