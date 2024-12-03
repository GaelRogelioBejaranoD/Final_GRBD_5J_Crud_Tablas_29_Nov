from django.urls import path
from membresia_app import views

urlpatterns = [
    path("inicio_vistaMembresia", views.inicio_vistaMembresia, name="inicio_vistaMembresia"),
    path("registrarMembresia/", views.registrarMembresia, name="registrarMembresia"),
    path("seleccionarMembresia/<id_mem>", views.seleccionarMembresia, name="seleccionarMembresia"),
    path("editarMembresia/", views.editarMembresia, name="editarMembresia"),
    path("borrarMembresia/<id_mem>", views.borrarMembresia, name="borrarMembresia"),
]
