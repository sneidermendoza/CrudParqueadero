from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarVehiculo/',views.registrarVehiculo),
    path('edicionVehiculo/<placa>',views.edicionVehiculo),
    path('editarVehiculo/',views.editarVehiculo),
    path('salidaParqueadero/<placa>',views.salidaParqueadero),
]