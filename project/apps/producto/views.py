from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import models
from . import forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "producto/index.html")

def producto_categoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    context = {"categorias":categorias}
    return render(request, "producto/producto_categoria_list.html", context)

def producto_categoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoCategoriaForm()
        return render(request, "producto/producto_categoria_create.html", {"form":form})
    
def producto_create(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoForm()
        return render(request, "producto/producto_create.html",  {"form":form}) 
    
def producto_list(request):
    productos = models.Producto.objects.all()
    context = {"productos":productos}
    return render(request, "producto/producto_list.html", context)
