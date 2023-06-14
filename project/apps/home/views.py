from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# * Para el login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None: 
                login(request, user)
                return render(request, "home/index.html", {"mensaje" : f"¡Bienvenido {usuario}!"})
    else: 
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form":form})

