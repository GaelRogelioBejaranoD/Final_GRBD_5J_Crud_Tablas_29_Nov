from django.urls import path
from entrenador_app import views

urlpatterns = [
    path("inicio_vistaEntrenador", views.inicio_vistaEntrenador, name="inicio_vistaEntrenador"),
    path("registrarEntrenador/", views.registrarEntrenador, name="registrarEntrenador"),
    path("seleccionarEntrenador/<id_entrenador>", views.seleccionarEntrenador, name="seleccionarEntrenador"),
    path("editarEntrenador/", views.editarEntrenador, name="editarEntrenador"),
    path("borrarEntrenador/<id_entrenador>", views.borrarEntrenador, name="borrarEntrenador"),
]
