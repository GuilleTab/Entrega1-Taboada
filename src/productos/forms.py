from django.forms import Form, CharField

class FormularioBusqueda(Form):
    nombre_personal = CharField()
