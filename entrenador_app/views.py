from django.shortcuts import render, redirect
from .models import Entrenador

# Create your views here.
def inicio_vistaEntrenador(request):
    losentrenadores = Entrenador.objects.all()
    return render(request, "gestionarEntrenadores.html", {"misentrenadores": losentrenadores})

def registrarEntrenador(request):
    if request.method == 'POST':
        id_entrenador = request.POST["txtid_entrenador"]
        nombre = request.POST["txtnombre"]
        especialidad = request.POST["txtespecialidad"]
        telefono = request.POST["numtelefono"]
        email = request.POST["txtemail"]
        estado = request.POST.get("chkestado") == 'on'
        horario = request.POST["txthorario"]

        Entrenador.objects.create(
            id_entrenador=id_entrenador,
            nombre=nombre,
            especialidad=especialidad,
            telefono=telefono,
            email=email,
            estado=estado,
            horario=horario
        )
    return redirect("inicio_vistaEntrenador")

def seleccionarEntrenador(request, id_entrenador):
    entrenador = Entrenador.objects.get(id_entrenador=id_entrenador)
    return render(request, "editarEntrenador.html", {"misentrenadores": entrenador})

def editarEntrenador(request):
    if request.method == 'POST':
        id_entrenador = request.POST["txtid_entrenador"]
        nombre = request.POST["txtnombre"]
        especialidad = request.POST["txtespecialidad"]
        telefono = request.POST["numtelefono"]
        email = request.POST["txtemail"]
        estado = request.POST.get("chkestado") == 'on'
        horario = request.POST["txthorario"]

        entrenador = Entrenador.objects.get(id_entrenador=id_entrenador)
        entrenador.nombre = nombre
        entrenador.especialidad = especialidad
        entrenador.telefono = telefono
        entrenador.email = email
        entrenador.estado = estado
        entrenador.horario = horario
        entrenador.save()

    return redirect("inicio_vistaEntrenador")

def borrarEntrenador(request, id_entrenador):
    entrenador = Entrenador.objects.get(id_entrenador=id_entrenador)
    entrenador.delete()
    return redirect("inicio_vistaEntrenador")
