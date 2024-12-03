from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def inicio_vistaProducto(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre_producto = request.POST["txtnombre_producto"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    stock = request.POST["numstock"]
    tipo = request.POST["txttipo"]

    Producto.objects.create(
        id_producto=id_producto,
        nombre_producto=nombre_producto,
        descripcion=descripcion,
        precio=precio,
        stock=stock,
        tipo=tipo
    )
    return redirect("inicio_vistaProducto")

def seleccionarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": producto})

def editarProducto(request):
    if request.method == 'POST':
        id_producto = request.POST["txtid_producto"]
        nombre_producto = request.POST["txtnombre_producto"]
        descripcion = request.POST["txtdescripcion"]
        precio = request.POST["numprecio"]
        stock = request.POST["numstock"]
        tipo = request.POST["txttipo"]

        producto = Producto.objects.get(id_producto=id_producto)
        producto.nombre_producto = nombre_producto
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.tipo = tipo
        producto.save()

    return redirect("inicio_vistaProducto")

def borrarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("inicio_vistaProducto")
