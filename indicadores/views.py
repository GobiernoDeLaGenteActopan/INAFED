from django.shortcuts import render
from django import views
from .models import Indicador


class Dashboard(views.View):

    def get(self, request):
        template_name="indicadores/dashboard.html"

        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Pésimo"))
        print(total)

        context = {'total':total,
                   'verde':verde,
                   'amarillo':amarillo,
                  'rojo':rojo}

        return render(request, template_name, context)


class indicadoresListView(views.View):
    pass


class indicadoresDetailView(views.View):
    pass