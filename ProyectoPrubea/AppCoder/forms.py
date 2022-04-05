from django import forms

class personaFormulario(forms.Form):
    
    nombre= forms.CharField()
    edad=forms.IntegerField()
    fechaNac = forms.DateField()  

class productosFormulario(forms.Form):

    nombre= forms.CharField()
    stocknum=forms.IntegerField()
    stock=forms.CharField()

class horarioFormulario(forms.Form):

    entrada= forms.IntegerField()
    salida= forms.IntegerField()