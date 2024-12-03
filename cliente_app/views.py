from django.shortcuts import render,redirect
from .models import Cliente

# Create your views here.
def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    membresia_activa='chkactivo' in request.POST
    dias_restantes_mem=request.POST["numdias"]
    fecha_ingreso=request.POST["dateregistro"]
    

    guardarcliente=Cliente.objects.create(
        id_cliente=id_cliente,nombre=nombre, email=email,telefono=telefono,membresia_activa=membresia_activa,dias_restantes_mem=dias_restantes_mem,fecha_ingreso=fecha_ingreso,
    ) # GUARDA EL REGISTRO

    return redirect("cliente")

def seleccionarCliente(request,codigo):
    cliente=Cliente.objects.get(id_cliente=codigo)
    fecha_fin=cliente.fecha_ingreso.strftime('%Y-%m-%d')
    return render(request,"editarcliente.html",{"misclientes":cliente, "misclientes" : cliente, "fecha_fin" : fecha_fin})

def editarCliente(request):
    id_cliente=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    membresia_activa='chkactivo' in request.POST
    dias_restantes_mem=request.POST["numdias"]
    fecha_ingreso=request.POST["dateregistro"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.email=email
    cliente.telefono=telefono
    cliente.membresia_activa=membresia_activa
    cliente.dias_restantes_mem=dias_restantes_mem
    cliente.fecha_ingreso=fecha_ingreso
    
    cliente.save() # guarda registro actualizado
    return redirect("cliente")

def borrarCliente(request,codigo):
    cliente=Cliente.objects.get(id_cliente=codigo)
    cliente.delete() # borra el registro
    return redirect("cliente")