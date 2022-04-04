from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import persona
from AppCoder.forms import personaFormulario

# Create your views here.
def persona1(request):
    # mi_persona=persona(nombre=nombre,edad=edad)
    # mi_persona.save()
    
    return HttpResponse(f"se genero el La persona " )

def listar_Personas(request):
    personas=persona.objects.all()
    contexto={'personas':personas}
    return render (request,"AppCoder/listaPersonas.html",contexto)

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def agregarPersonas(request):
    return render (request,"AppCoder/agregarPersonas.html")

def agregarProducto(request):
    return render (request,"AppCoder/agregarProducto.html")

def personaFormulario(request):

    if request.method == 'POST':

        print(request.POST)

        mi_formulario = personaFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            nombre= informacion['nombre']
            edad= informacion['edad']
            fechaNac= informacion['fechaNac']

            mi_curso = persona(nombre = nombre, edad = edad, fechaNac = fechaNac)
            mi_curso.save()
            
        return render(request, 'AppCoder/inicio.html', {'nombre': nombre, 'edad': edad})

    else:

        mi_formulario = personaFormulario(  )

    return render(request, 'AppCoder/personaFormulario.html', {'miForm': mi_formulario})
    
    
    