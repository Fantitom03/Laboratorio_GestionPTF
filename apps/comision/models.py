from django.db import models
from apps.persona.models import Docente

class Miembro_CSTF (Docente):
    resolucion_asignacion = models.IntegerField(unique=True)
    fecha_alta = models.DateField()

class Miembro_TE (Docente):

    rol = models.CharField(max_length=100)
    fecha_alta = models.DateField()


class TribunalEvaluador (models.Model):
    miembros = models.ManyToManyField(Miembro_TE)
    fecha_disposicion = models.DateField()
    numero_disposicion = models.IntegerField(unique=True)
    archivo_disposicion = models.FileField()