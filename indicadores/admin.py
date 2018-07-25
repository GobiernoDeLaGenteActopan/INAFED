from django.contrib import admin
from .models import Indicador, Evidencia, Subevidencia, Seguimiento


class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'nombre', 'status']
    list_filter = ['status','area']
    actions = ['make_insatisfactorio', 'make_satisfactorio', 'make_regular', 'make_ncs']

    def make_insatisfactorio(self, request, queryset):
        queryset.update(status="Insatisfactorio")

    def make_satisfactorio(self, request, queryset):
        queryset.update(status="Satisfactorio")

    def make_regular(self, request, queryset):
        queryset.update(status="Regular")

    def make_ncs(self, request, queryset):
        queryset.update(status="NCS")

    make_insatisfactorio.short_description = "Colocar como Insatisfactorio"
    make_satisfactorio.short_description = "Colocar como Satisfactorio"
    make_regular.short_description = "Colocar como Regular"
    make_ncs.short_description = "Colocar como NCS"

admin.site.register(Indicador, IndicadorAdmin)
#admin.site.register(Evidencia)
#admin.site.register(Subevidencia)
#admin.site.register(Seguimiento)
