from django.shortcuts import render
from django import views
from .models import Indicador


class Dashboard(views.View):

    def get(self, request):
        template_name="indicadores/dashboard.html"
        indicadores = Indicador.objects.filter(area=request.user)

        context = {'indicadores':indicadores}

        return render(request, template_name, context)


class indicadoresListView(views.View):
    pass


class indicadoresDetailView(views.View):
    pass