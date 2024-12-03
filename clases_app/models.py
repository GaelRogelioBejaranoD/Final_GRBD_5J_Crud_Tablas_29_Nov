from django.db import models

# Create your models here.
class Clase(models.Model):
    id_clase=models.PositiveIntegerField(primary_key=True)
    id_entrenador=models.PositiveIntegerField()
    nombre_clase=models.CharField(max_length=50)
    horario=models.CharField(max_length=100)
    capacidad=models.PositiveIntegerField()
    ubicacion=models.CharField(max_length=100)
    costo=models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return self.nombre