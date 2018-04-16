from django.contrib import admin
from .models import Indicador, Evidencia, Subevidencia, Seguimiento

admin.site.register(Indicador)
admin.site.register(Evidencia)
admin.site.register(Subevidencia)
admin.site.register(Seguimiento)
# Register your models here.
