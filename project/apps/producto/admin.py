from django.contrib import admin
from . import models

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",) 
    list_filter = ("nombre",)
    ordering = ("nombre",)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "medida", "descripcion")
