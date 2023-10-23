from django.db import models
from apps.persona.models import Docente, Alumno

"""
alumnos, fecha de alta alumno, director, fecha de alta director, co-director, 
fecha de alta co-director, asesor (opcional), fecha de alta asesor (opcional), título del PTF, 
descripción, fecha de presentación, archivos adjuntos de: PTF, certificado analítico, 
nota de aceptación de director y currículum vitae del asesor. 
"""

class Proyecto_TF (models.Model):
    fecha_alta_alumno = models.DateField()
    director = models.OneToOneField(Docente, related_name='director_proyecto', on_delete=models.CASCADE)
    fecha_alta_director = models.DateField()
    co_director = models.OneToOneField(Docente, related_name='codirector_proyecto', on_delete=models.CASCADE)
    fecha_alta_co_director = models.DateField()
    asesor = models.OneToOneField(Docente, related_name='asesor_proyecto', null=True, blank=True,
                               on_delete=models.CASCADE)
    fecha_alta_asesor = models.DateField(null=True, blank=True)
    titulo_ptf = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_presentacion = models.DateField()
    archivos_adjuntos_ptf = models.FileField()
    certificado_analitico = models.FileField()
    nota_aceptacion_director = models.FileField()
    #estado y agregar que pueda tomar ciertos valores determinados
    #observaciones

    def __str__(self):
        return f'Proyecto TF de {self.matricula}'

"""
# Obtener todos los alumnos de un proyecto específico
proyecto = Proyecto_TF.objects.get(id=1)  # Reemplaza 1 con el ID del proyecto que deseas consultar
alumnos_del_proyecto = proyecto.alumnos.all()

# Iterar sobre los alumnos del proyecto
for alumno in alumnos_del_proyecto:
    print(alumno.nombre_completo)
"""

class Proyecto_TF_Alumno(models.Model):
    proyecto_tf = models.ForeignKey(Proyecto_TF, related_name='alumnos', on_delete=models.CASCADE, null=True, blank=True)
    alumno = models.ForeignKey('persona.Alumno', related_name='proyectos_tf', on_delete=models.CASCADE)

class Informe_TF(models.Model):
    alumno = models.ForeignKey('persona.Alumno', related_name='informe_tf', on_delete=models.CASCADE)
    archivo_itf = models.FileField(upload_to='archivos_itf/')
    proyecto_tf = models.ForeignKey(Proyecto_TF, related_name='informes_tf', on_delete=models.CASCADE)
    # estado y agregar que pueda tomar ciertos valores determinados
    # observaciones

    def __str__(self):
        return f'Informe TF de {self.matricula}'


#evaluaciones PTF, ITF y defensa