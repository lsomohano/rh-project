from django.urls import path
from proveedores import views

urlpatterns = [
    path('',views.proveedores, name="Proveedores"),
    path('create/',views.create, name="Create"),
]