from django.shortcuts import render
from .models import Auto

# Create your views here.
def home(request):
    autos = Auto.objects.all()# query para traernos todo lo de la tabla Auto
    return render(request, "CrudParqueadero.html", {"autos": autos})
