from django.urls import path
from . import views

urlpatterns = [
    path('',views.proveedores, name="Proveedores"),
    path('create/',views.createView, name="Create"),
    path('edit/<int:id>',views.editView, name="Edit"),
    path('details/<int:id>',views.detailsView, name="Details"),
]