from django.contrib import admin
from .models import Indicador, Evidencia, Subevidencia, Seguimiento


class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'nombre', 'status']
    list_filter = ['status']
    actions = ['make_insatisfactorio']

    def make_insatisfactorio(self, request, queryset):
        queryset.update(status="Insatisfactorio")
    make_insatisfactorio.short_description = "Colocar como status insatisfactorio"

admin.site.register(Indicador, IndicadorAdmin)
#admin.site.register(Evidencia)
#admin.site.register(Subevidencia)
#admin.site.register(Seguimiento)
