from django.shortcuts import render
from productos.models import Personal, Articulo, Vehiculos
from productos.forms import FormularioBusqueda

def index(request):

    listado_personal = Personal.objects.all()

    if request.GET.get("nombre"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_personal = listado_personal.filter(nombre__icontains = data["nombre_personal"])

        formulario = FormularioBusqueda()
        return render(request, "productos/index.html", {"personal": listado_personal, "formulario": formulario})

    else:
        formulario = FormularioBusqueda() 
        return render(request, "productos/index.html", {"personal": listado_personal, "formulario": formulario})


def articulos(request):
    listado_productos = Articulo.objects.all()

    if request.GET.get("nombre_articulo"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = listado_productos.filter(nombre__icontains = data["nombre_articulo"])

        formulario = FormularioBusqueda()
        return render(request, "productos/index.html", {"personal": listado_productos, "formulario": formulario})

    else:
        formulario = FormularioBusqueda() 
        return render(request, "productos/index.html", {"personal": listado_productos, "formulario": formulario})



def crear_articulo(request):

    if request.method =="GET":
        return render(request, "productos/formulario_producto.html")
    
    else:
        nombre = request.POST["nombre"]
        marca = request.POST["marca"]
        precio = request.POST["precio"]
        stock = request.POST["stock"]
        articulo = Articulo(nombre=nombre, marca=marca, precio=precio, stock=stock)
        articulo.save()
        return render(request, "productos/index.html")

    

def crear_miembro(request):

    if request.method =="GET":
        return render(request, "productos/formulario_miembro.html")
    
    else:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        puesto = request.POST["puesto"]
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        año_ingreso = request.POST["año_ingreso"]
        personal = Personal(nombre=nombre, apellido=apellido, puesto=puesto, fecha_nacimiento=fecha_nacimiento, año_ingreso=año_ingreso)
        personal.save()
        return render(request, "productos/index.html")


def crear_vehiculo(request):

    if request.method =="GET":
        return render(request, "productos/formulario_vehiculos.html")
    
    else:
        tipo_vehiculo = request.POST["tipo_vehiculo"]
        patente_vehiculo = request.POST["patente_vehiculo"]
        estado_vehiculo = request.POST["estado_vehiculo"]
        fecha_service = request.POST["fecha_service"]
        vehiculo = Vehiculos(tipo_vehiculo=tipo_vehiculo, patente_vehiculo=patente_vehiculo, estado_vehiculo=estado_vehiculo, fecha_service=fecha_service)
        vehiculo.save()
        return render(request, "productos/base.html")   
