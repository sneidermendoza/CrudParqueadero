from django.db import models

# Create your models here.
class Auto(models.Model):
    placa = models.CharField(primary_key=True, max_length=6)
    tipo_vehiculo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self): #metodo para mostrar lo que tiene la clase
        texto = "{0} ({1})"
        return texto.format(self.placa, self.color)
