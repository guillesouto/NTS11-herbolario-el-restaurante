from django.shortcuts import render
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioPlatos import FormularioPlatos
from web.models import Platos
from web.models import Empleados
# Create your views here.

#todas las vistas son funciones de python

def Home(request):
    return render(request, 'home.html')

def PlatosVista(request):

    #Esta vista va a utilizar un formulario de django
    # debo crear entonces un objeto de la clase FormularioPlatos
    formulario=FormularioPlatos()

    #Creamos un Diccionario Para enviar el formulario al HTML(template)
    data={
        'formulario':formulario
    }

    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #Construir un diccionario de envio de datos hacia ala BD
            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
                
            
                

            #intentare llevar mis datos a la base de Datos
            try:
                platoNuevo.save()
                print("exito Guardando....")
            except Exception as error:
                print("uppsss..",error)

    return render(request, 'menuplatos.html', data)

def EmpleadosVista(request):
    #Esta vista va a utilizar un formulario de django
    # debo crear entonces un objeto de la clase FormularioEmpleados
    formulario=FormularioEmpleados()

    #Creamos un Diccionario Para enviar el formulario al HTML(template)
    data={
        'formulario':formulario
    }

    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario=FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #Construir un diccionario de envio de datos hacia ala BD
            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombre"],
                apellidos = datosLimpios["apellidos"],
                fotografia =datosLimpios["fotografia"],
                tipo=datosLimpios["tipo"],
                salario = datosLimpios["salario"],
                contacto = datosLimpios["contacto"]
            )
            #intentare llevar mis datos a la base de Datos
            try:
                empleadoNuevo.save()
                print("exito Guardando....")
            except Exception as error:
                print("uppsss..",error)
    return render(request, 'registrarEmpleados.html', data)

