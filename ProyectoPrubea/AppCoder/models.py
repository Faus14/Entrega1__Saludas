from django.db import models

# Create your models here.
class persona(models.Model):
    
    nombre= models.CharField('nombre',max_length=25)
    edad=models.IntegerField('edad')
    fechaNac = models.DateField('fechaNac', auto_now= False, auto_now_add=False, blank=True, null=True)  

    def __str__(self) -> str:
        return f'{self.nombre}'
        
class horario(models.Model):
    
    entrada= models.IntegerField('entrada')
    salida=models.IntegerField('salida')
    
class producto(models.Model):
    
    nombre= models.CharField('nombre',max_length=25)
    stocknum= models.IntegerField('stocknum')
    stock=models.CharField('stock', max_length=30)
    
    

