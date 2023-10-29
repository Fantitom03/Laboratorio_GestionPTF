from django.db import models

class Persona (models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
        # O usando str.format():
        # return "{} {}".format(self.nombre, self.apellido)

    def __str__(self):
        return '{}'.format(self.nombre_completo)

class Docente (Persona):
    cuil = models.CharField(max_length=11, unique=True)

class Alumno (Persona):
    matricula = models.CharField(max_length=5, unique=True)
    correo_electronico = models.EmailField(max_length=254)

class Asesor (Persona):
    curriculum = models.FileField()



