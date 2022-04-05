from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

from .models import persona, producto, horario
from AppCoder.forms import personaFormulario, horarioFormulario, productosFormulario
from django.http.request import QueryDict


# Create your views here.
def persona1(request):
    # mi_persona=persona(nombre=nombre,edad=edad)
    # mi_persona.save()
    
    return HttpResponse(f"se genero el La persona " )

def listar_Personas(request):
    personas=persona.objects.all()
    contexto={'personas':personas}
    return render (request,"AppCoder/agregarPersonas.html",contexto)

def inicio(request):
    return render (request, "AppCoder/inicio.html")
    
def personas(request):
    
   

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
            personas=persona.objects.all()
            contexto={'personas':personas}
        return render (request,"AppCoder/agregarPersonas.html",contexto) 
        


    else:

        mi_formulario = personaFormulario(  )

    return render(request, 'AppCoder/personaFormulario.html', {'miForm': mi_formulario})
    
def productos (request):

    if request.method == 'POST':

        print(request.POST)

        mi_formulario = productosFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            nombre= informacion['nombre']
            stocknum= informacion['stocknum']
            stock= informacion['stock']

            mi_app = producto(nombre = nombre, stocknum = stocknum, stock = stock)
            mi_app.save()
            producto1=producto.objects.all()
            contexto3={'productos':producto1}
        return render (request,"AppCoder/agregarProducto.html",contexto3) 
            
        

    else:

        mi_formulario = productosFormulario()

    return render(request, 'AppCoder/productosFormulario.html', {'miForm': mi_formulario})


def horarios(request):

    if request.method == 'POST':

        print(request.POST)

        mi_formulario = horarioFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            entrada= informacion['entrada']
            salida= informacion['salida']

            mi_horario = horario(entrada = entrada, salida = salida)
            mi_horario.save()
            horarios2=horario.objects.all()
            contexto2={'horario':horarios2}
        return render (request,"AppCoder/agregarHorario.html",contexto2) 
            
        

    else:

        mi_formulario = horarioFormulario()

    return render(request, 'AppCoder/horarioFormulario.html', {'miForm': mi_formulario})