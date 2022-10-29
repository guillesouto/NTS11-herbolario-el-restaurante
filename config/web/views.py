from django.shortcuts import render
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioPlatos import FormularioPlatos
# Create your views here.

#todas las vistas son funciones de python

def Home(request):
    return render(request, 'home.html')

def Platos(request):

    #Esta vista va a utilizar un formulario de django
    # debo crear entonces un objeto de la clase FormularioPlatos
    formulario=FormularioPlatos()

    #Creamos un Diccionario Para enviar el formulario al HTML(template)
    data={
        'formulario':formulario
    }

    return render(request, 'menuplatos.html', data)

def Empleados(request):
    #Esta vista va a utilizar un formulario de django
    # debo crear entonces un objeto de la clase FormularioEmpleados
    formulario=FormularioEmpleados()

    #Creamos un Diccionario Para enviar el formulario al HTML(template)
    data={
        'formulario':formulario
    }
    return render(request, 'registrarEmpleados.html', data)

