from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import models
from . import forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "sucursales/index.html")

def sucursal_create(request):
    if request.method == "POST":
        form = forms.SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sucursales:index")
    else:
        form = forms.SucursalForm()
        return render(request, "sucusales/sucusal_create.html", {"form":form}) 
    
def sucursal_list(request):
    sucursales = models.Sucursal.objects.all()
    context = {"sucursales":sucursales}
    return render(request, "sucursales/sucursal_list.html", context)
