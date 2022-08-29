from django.urls import path
from reclutamiento import views

urlpatterns = [
    path('',views.home, name="Home"),
]