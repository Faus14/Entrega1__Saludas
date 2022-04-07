from django.urls import include, path
from AppCoder import views
from .views import inicio

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('persona/',views.listar_Personas),
    path('personaFormulario/',views.personas,name="personaFormulario"),
    path('productosFormulario/',views.productos, name="productosFormulario"),
    path('horarioFormulario/',views.horarios, name="horarioFormulario"),
    path('busquedaPersona/',views.busquedaPersona, name="busquedaPersona"),
    path('buscar/',views.buscar, name="buscar")

]
