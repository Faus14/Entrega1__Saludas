from django.urls import include, path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio),
    path('persona/',views.listar_Personas),
    path('personaFormulario/',views.personas,name="Persona"),
    path('productosFormulario/',views.productos, name="Productos"),
    path('horarioFormulario/',views.horarios, name="Horarios"),
]
