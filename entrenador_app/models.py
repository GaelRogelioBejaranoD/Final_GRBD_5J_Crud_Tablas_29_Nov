from django.db import models

# Create your models here.
class Entrenador(models.Model):
    id_entrenador=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=50)
    estado=models.BooleanField()
    horario=models.CharField(max_length=100)

    
    def __str__(self):
        return self.nombre