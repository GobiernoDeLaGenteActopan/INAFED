from django.db import models
from django.contrib.auth.models import User

choices_nivel = (
        ('Gestión', 'Gestión'),
        ('Desempeño', 'Desempeño'),
    )

choices_status = (
    ('#2ecc71', 'Satisfactorio'),
    ('#2ecc71', 'Regular'),
    ('#2ecc71', 'Pésimo')
)


class Indicador(models.Model):

    indicador = models.CharField(max_length=10)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.CharField(max_length=15, choices=choices_nivel, blank=True, null=True)
    dimension = models.CharField(max_length=144, blank=True, null=True)
    criterios_evaluacion = models.TextField(blank=True, null=True)
    area = models.ForeignKey(User, related_name='indicadores', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=choices_status)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.indicador + ' - ' + self.nombre


class Evidencia(models.Model):

    indicador = models.ForeignKey(Indicador, related_name="evidencias", on_delete=models.CASCADE)
    titulo = models.TextField()
    porcentaje_total = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    porcentaje_real = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    archivo = models.FileField(upload_to='evidencias/', blank=True, null=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.indicador.indicador + ' - ' + self.titulo


class Subevidencia(models.Model):

    evidencia = models.ForeignKey(Evidencia, related_name="subevidencias", on_delete=models.CASCADE)
    titulo = models.TextField()
    porcentaje = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    archivo = models.FileField(upload_to='evidencias/', blank=True, null=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.indicador.indicador + ' - ' + self.evidencia.titulo + ' - ' + self.titulo


class Seguimiento(models.Model):

    indicador = models.ForeignKey(Indicador, related_name="seguimientos", on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.indicador.indicador + ' - ' + self.cuerpo

