from django.db import models

from categorias.models import Categoria
# Create your models here.

class Elementos(models.Model):

    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=14,decimal_places=2)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f" {self.descripcion} {self.precio}"