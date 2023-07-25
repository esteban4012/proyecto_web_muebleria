from django.db import models

from ordenes.models import Orden

from elementos.models import Elementos

# Create your models here.

class Movimiento(models.Model):

    id = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    valor_total = models.DecimalField(max_digits=15,decimal_places=2)
    id_orden = models.ForeignKey(Orden,on_delete=models.CASCADE)
    id_elemento = models.ForeignKey(Elementos,on_delete=models.CASCADE)

    
    
    def __str__(self) -> str:
        return f"{self.cantidad} {self.id_elemento.descripcion} {self.valor_total} {self.id_orden} "