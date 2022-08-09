from django.shortcuts import render
from productos.models import Personal
from productos.forms import FormularioBusqueda

def index(request):

    listado_personal = Personal.objects.all()

    if request.GET.get("nombre_personal"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_personal = listado_personal.filter(nombre__icontains = data["nombre_personal"])

        formulario = FormularioBusqueda()
        return render(request, "productos/index.html", {"personal": listado_personal, "formulario": formulario})

    else:
        formulario = FormularioBusqueda() 
        return render(request, "productos/index.html", {"personal": listado_personal, "formulario": formulario})

    

    
