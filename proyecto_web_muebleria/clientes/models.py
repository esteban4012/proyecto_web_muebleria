from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    apellido_2 = models.CharField(max_length=20, blank=True,null=True)
    numero_identificacion = models.IntegerField()
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero_identificacion}"
    
