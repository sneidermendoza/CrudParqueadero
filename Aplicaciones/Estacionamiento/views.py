from django.shortcuts import render, redirect
from .models import Auto


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroFormulario

# Create your views here.
def home(request):
    autos = Auto.objects.all()# query para traernos todo lo de la tabla Auto
    return render(request, "CrudParqueadero.html", {"autos": autos})

def registrarVehiculo(request):
    placa= request.POST['txtPlaca']
    color= request.POST['txtColor']
    tipo_vehiculo = request.POST['txtTipoDeVehiculo']

    auto = Auto.objects.create(placa=placa, color=color, tipo_vehiculo=tipo_vehiculo)
    return redirect('/')

def edicionVehiculo(request, placa):
    auto = Auto.objects.get(placa=placa)
    return render(request, 'edicionVehiculo.html', {"auto":auto})

def editarVehiculo(request):
    placa= request.POST['txtPlaca']
    color= request.POST['txtColor']
    tipo_vehiculo = request.POST['txtTipoDeVehiculo']

    auto = Auto.objects.get(placa=placa)
    auto.placa = placa
    auto.color = color
    auto.tipo_vehiculo = tipo_vehiculo
    auto.save()
    return redirect('/')

def salidaParqueadero(request, placa):
    auto = Auto.objects.get(placa=placa)
    auto.delete()
    return redirect('/')

def acceso(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        contraceña = request.POST.get('contraceña')

        user = authenticate(username=usuario, password=contraceña)
        if user:
            login(request, user)
            messages.success(request, f"Bienvenido. {user.username}")
            return redirect('/')
        else:
            messages.error(request, "Usuario o contraseña invalido")

    return render(request, 'usuarios/login.html', {

    })

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect('login')

def registro(request):
    formulario = RegistroFormulario(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        user = formulario.save()

        if user:
            login(request, user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('/')

    return render(request, 'usuarios/register.html', {
        'formulario': formulario
    })