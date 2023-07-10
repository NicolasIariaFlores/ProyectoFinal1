from django.db import models
    
"""class PaisSucursal(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
"""
class Sucursal(models.Model):
    #pais = models.ForeignKey(PaisSucursal, on_delete=models.SET_NULL, null=True)
    ciudad = models.CharField(max_length=100, unique=False)
    calle = models.CharField(max_length=100, unique=False)
    altura = models.CharField(max_length=100, unique=False)
    numero_sucursal = models.CharField(max_length=20, unique=True)