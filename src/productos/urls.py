from django.urls import path
from productos.views import *

urlpatterns = [
    path("inicio/", index, name="inicio"),
    path("articulos/", articulos, name="articulos"),
    path("personal/", index, name="personal"),
    path("crear/articulo/", crear_articulo, name="crear_articulo"),
    path("crear/miembro/", crear_miembro, name="crear_miembro"),
    path("crear/vehiculo/", crear_vehiculo, name="crear_vehiculo"),
    
]