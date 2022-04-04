from django import forms

class personaFormulario(forms.Form):
    
    nombre= forms.CharField()
    edad=forms.IntegerField()
    fechaNac = forms.DateField()  