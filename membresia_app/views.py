from django.shortcuts import render, redirect
from .models import Membresia

# Create your views here.
def inicio_vistaMembresia(request):
    lasmembresias = Membresia.objects.all()
    return render(request, "gestionarMembresias.html", {"mismembresias": lasmembresias})

def registrarMembresia(request):
    id_mem = request.POST["txtid_mem"]
    id_cliente = request.POST["txtid_cliente"]
    duracion = request.POST["txtduracion"]
    tipo = request.POST["txttipo"]
    costo = request.POST["txtcosto"]
    descuentos = request.POST["txtdescuentos"]

    guardarmembresia = Membresia.objects.create(
        id_mem=id_mem, id_cliente=id_cliente, duracion=duracion, tipo=tipo, costo=costo, descuentos=descuentos
    )  # Guarda el registro

    return redirect("inicio_vistaMembresia")

def seleccionarMembresia(request, id_mem):
    lasmembresias = Membresia.objects.get(id_mem=id_mem)
    return render(request, "editarMembresias.html", {"mismembresias": lasmembresias})

def editarMembresia(request):
    id_mem = request.POST["txtid_mem"]
    id_cliente = request.POST["txtid_cliente"]
    duracion = request.POST["txtduracion"]
    tipo = request.POST["txttipo"]
    costo = request.POST["txtcosto"]
    descuentos = request.POST["txtdescuentos"]

    membresia = Membresia.objects.get(id_mem=id_mem)
    membresia.id_cliente = id_cliente
    membresia.duracion = duracion
    membresia.tipo = tipo
    membresia.costo = costo
    membresia.descuentos = descuentos
    membresia.save()  # Guarda el registro actualizado
    return redirect("inicio_vistaMembresia")

def borrarMembresia(request, id_mem):
    membresia = Membresia.objects.get(id_mem=id_mem)
    membresia.delete()  # Borra el registro
    return redirect("inicio_vistaMembresia")
