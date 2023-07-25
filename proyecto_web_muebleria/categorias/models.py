from django.db import models

# Create your models here.

class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.descripcion}"