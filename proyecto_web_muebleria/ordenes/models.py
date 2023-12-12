from django.db import models

from clientes.models import Cliente

from elementos.models import Elementos

# Create your models here.

class Orden(models.Model):
    
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cantidad = models.DecimalField(max_digits=4, decimal_places=0, null=False)
    valor_total = models.DecimalField(max_digits=15,decimal_places=2, null=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_elemento = models.ForeignKey(Elementos,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.id_cliente.nombre} {self.id_elemento.descripcion} {self.fecha} " 