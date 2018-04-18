from django.shortcuts import render
from django import views
from .models import Indicador
from django.views.generic.list import ListView

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

    def get(self, request):

        template_name="indicadores/indicador_list.html"

        indicadores = Indicador.objects.filter(area=request.user)
        print(len(indicadores))
        context = {'indicadores':indicadores, 'tab': 'all'}

        return render(request, template_name, context)

class SatisfactorioList(views.View):

    def get(self, request):

        template_name = "indicadores/indicador_list.html"

        indicadores = Indicador.objects.filter(area=request.user, status="Satisfactorio")

        context = {'indicadores': indicadores, 'tab': 'green'}

        return render(request, template_name, context)

class RegularList(views.View):

    def get(self, request):
        template_name = "indicadores/indicador_list.html"

        indicadores = Indicador.objects.filter(area=request.user, status="Regular")

        context = {'indicadores': indicadores, 'tab': 'yellow'}

        return render(request, template_name, context)

class PesimoList(views.View):

    def get(self, request):
        template_name = "indicadores/indicador_list.html"

        indicadores = Indicador.objects.filter(area=request.user, status="Pésimo")

        context = {'indicadores': indicadores, 'tab': 'red'}

        return render(request, template_name, context)



class indicadoresDetailView(views.View):
    pass