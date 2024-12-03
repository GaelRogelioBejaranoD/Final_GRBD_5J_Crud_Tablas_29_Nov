from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    telefono=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    membresia_activa=models.BooleanField()
    dias_restantes_mem=models.PositiveIntegerField()
    fecha_ingreso=models.DateField(null=False,blank=False)

    
    def __str__(self):
        return self.nombre