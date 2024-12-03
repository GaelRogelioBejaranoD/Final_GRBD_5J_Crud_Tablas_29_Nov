from django.shortcuts import render, redirect
from .models import Clase

# Create your views here.
def inicio_vistaClase(request):
    lasclases = Clase.objects.all()
    return render(request, "gestionarClases.html", {"misclases": lasclases})

def registrarClase(request):
    if request.method == 'POST':
        id_clase = request.POST["txtid_clase"]
        nombre_clase = request.POST["txtnombre_clase"]
        horario = request.POST["txthorario"]
        capacidad = request.POST["numcapacidad"]
        ubicacion = request.POST["txtubicacion"]
        costo = request.POST["numcosto"]
        id_entrenador = request.POST["numid_entrenador"]

        Clase.objects.create(
            id_clase=id_clase,
            nombre_clase=nombre_clase,
            horario=horario,
            capacidad=capacidad,
            ubicacion=ubicacion,
            costo=costo,
            id_entrenador=id_entrenador
        )
    return redirect("inicio_vistaClase")

def seleccionarClase(request, id_clase):
    clase = Clase.objects.get(id_clase=id_clase)
    return render(request, "editarClase.html", {"misclases": clase})

def editarClase(request):
    if request.method == 'POST':
        id_clase = request.POST["txtid_clase"]
        nombre_clase = request.POST["txtnombre_clase"]
        horario = request.POST["txthorario"]
        capacidad = request.POST["numcapacidad"]
        ubicacion = request.POST["txtubicacion"]
        costo = request.POST["numcosto"]
        id_entrenador = request.POST["numid_entrenador"]

        clase = Clase.objects.get(id_clase=id_clase)
        clase.nombre_clase = nombre_clase
        clase.horario = horario
        clase.capacidad = capacidad
        clase.ubicacion = ubicacion
        clase.costo = costo
        clase.id_entrenador = id_entrenador
        clase.save()

    return redirect("inicio_vistaClase")

def borrarClase(request, id_clase):
    clase = Clase.objects.get(id_clase=id_clase)
    clase.delete()
    return redirect("inicio_vistaClase")
