from django.db import models

# Create your models here.

class Mascota(models.Model):
    codigo = models.SmallIntegerField()
    nombre = models.CharField(max_length=20)
    tamano = models.FloatField()
    peso = models.FloatField()
    color = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    fecha_rescate = models.DateTimeField()
    tipo_estado = (('Rescatado','Rescatado'),
                   ('Disponibilidad','Disponibilidad'),
                   ('Adoptado','Adoptado')
    )
    estado = models.CharField(max_length=30,choices=tipo_estado)

    def nombre_mascota(self):
        cadena= "{0}"
        return cadena.format(self.nombre)

    def __str__(self):
        return self.nombre_mascota()