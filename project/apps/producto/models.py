from django.db import models

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "categoria de productos"
        verbose_name_plural = "categorias de productos"


    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    medida = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True)
    #imagen = models.ImageField(upload_to="photos", default=None)

    def __str__(self) -> str:
        return self.nombre

