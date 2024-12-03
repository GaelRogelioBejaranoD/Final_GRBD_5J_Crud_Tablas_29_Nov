from django.urls import path
from clases_app import views

urlpatterns = [
    path("inicio_vistaClase", views.inicio_vistaClase, name="inicio_vistaClase"),
    path("registrarClase/", views.registrarClase, name="registrarClase"),
    path("seleccionarClase/<id_clase>", views.seleccionarClase, name="seleccionarClase"),
    path("editarClase/", views.editarClase, name="editarClase"),
    path("borrarClase/<id_clase>", views.borrarClase, name="borrarClase"),
]
