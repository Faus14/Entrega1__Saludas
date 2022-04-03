from django.db import models

# Create your models here.
class persona(models.Model):
    
    nombre= models.CharField('nombre',max_length=25)
    edad=models.IntegerField('edad')
    fechaNac = models.DateField('fechaNac')  
    

