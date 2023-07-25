from django.db import models

from clientes.models import Cliente

# Create your models here.

class Orden(models.Model):
    
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_cliente.nombre} {self.fecha} " 