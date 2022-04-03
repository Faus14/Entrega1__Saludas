from django.http import HttpResponse
from django.shortcuts import render
from .models import persona

# Create your views here.
def persona1(request):
    # mi_persona=persona(nombre=nombre,edad=edad)
    # mi_persona.save()
    
    return HttpResponse(f"se genero el La persona " )

def listar_Personas(request):
    personas=persona.objects.all()
    contexto={'personas':personas}
    return render (request,"AppCoder/listaPersonas.html",contexto)
    