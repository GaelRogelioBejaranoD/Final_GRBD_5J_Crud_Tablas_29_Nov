from django.db import models

# Create your models here.
class Membresia(models.Model):
    id_mem=models.PositiveIntegerField(primary_key=True)
    id_cliente=models.PositiveIntegerField()
    duracion=models.PositiveIntegerField()
    tipo=models.CharField(max_length=50)
    costo=models.DecimalField(max_digits=10, decimal_places=2)
    descuentos=models.CharField(max_length=100)

    
    def __str__(self):
        return self.nombre