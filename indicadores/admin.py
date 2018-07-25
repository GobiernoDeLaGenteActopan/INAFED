from django.contrib import admin
from .models import Indicador, Evidencia, Subevidencia, Seguimiento


class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'nombre', 'status']
    list_filter = ['status']

admin.site.register(Indicador, IndicadorAdmin)
#admin.site.register(Evidencia)
#admin.site.register(Subevidencia)
#admin.site.register(Seguimiento)
