from django.shortcuts import render
from django import views
from .models import Indicador, Evidencia
from django.db.models import Q

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
        print("LLEGO A TODOS")
        template_name="indicadores/indicador_list.html"

        q = request.GET.get('q')
        print(q)
        indicadores = Indicador.objects.filter(area=request.user)

        if q:
            indicadores = Indicador.objects.filter(Q(area=request.user),
                                                    Q(nombre__icontains=q)|
                                                    Q(indicador__icontains=q)|
                                                     Q(descripcion__icontains=q)).distinct()

        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Pésimo"))

        context = {'indicadores':indicadores,
                   'tab': 'all',
                   'total': total,
                   'verde': verde,
                   'amarillo': amarillo,
                   'rojo': rojo
                   }

        return render(request, template_name, context)

class SatisfactorioList(views.View):

    def get(self, request):
        print("LLEGO A VERDE")
        template_name = "indicadores/indicador_list.html"

        q = request.GET.get('q')
        indicadores = Indicador.objects.filter(area=request.user, status="Satisfactorio")

        if q:
            indicadores = Indicador.objects.filter(Q(area=request.user),
                                                   Q(status="Satisfactorio"),
                                                   Q(nombre__icontains=q) |
                                                   Q(indicador__icontains=q) |
                                                   Q(descripcion__icontains=q)).distinct()


        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Pésimo"))

        context = {'indicadores': indicadores,
                   'tab': 'green',
                   'total': total,
                   'verde': verde,
                   'amarillo': amarillo,
                   'rojo': rojo
                   }

        return render(request, template_name, context)


class RegularList(views.View):

    def get(self, request):
        print("LLEGO A AMARILLO")
        template_name = "indicadores/indicador_list.html"
        q = request.GET.get('q')
        indicadores = Indicador.objects.filter(area=request.user, status="Regular")
        print(q)
        if q:
            indicadores = Indicador.objects.filter(Q(area=request.user),
                                                   Q(status="Regular"),
                                                   Q(nombre__icontains=q) |
                                                   Q(indicador__icontains=q) |
                                                   Q(descripcion__icontains=q)).distinct()

        print(indicadores)
        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Pésimo"))

        context = {'indicadores': indicadores,
                   'tab': 'yellow',
                   'total': total,
                   'verde': verde,
                   'amarillo': amarillo,
                   'rojo': rojo
                   }

        return render(request, template_name, context)

class PesimoList(views.View):

    def get(self, request):

        print("LLEGO A ROJO")
        template_name = "indicadores/indicador_list.html"
        q = request.GET.get('q')
        indicadores = Indicador.objects.filter(area=request.user, status="Pésimo")

        if q:
            indicadores = Indicador.objects.filter(Q(area=request.user),
                                                   Q(status="Pésimo"),
                                                   Q(nombre__icontains=q) |
                                                   Q(indicador__icontains=q) |
                                                   Q(descripcion__icontains=q)).distinct()


        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Pésimo"))

        context = {'indicadores': indicadores,
                   'tab': 'red',
                   'total': total,
                   'verde': verde,
                   'amarillo': amarillo,
                   'rojo': rojo
                   }

        return render(request, template_name, context)



class indicadoresDetailView(views.View):

    def get(self, request, pk):

        template_name="indicadores/indicador_detail.html"
        indicador = Indicador.objects.get(pk=pk)
        context = {'indicador':indicador}

        return render(request, template_name, context)


class EvidenciasDetailView(views.View):

    def get(self, request, pk, epk):

        template_name="indicadores/evidencia_detail.html"
        indicador = Indicador.objects.get(pk=pk)
        evidencia = Evidencia.objects.get(pk=epk, indicador=indicador)

        context = {'evidencia': evidencia}

        return render(request, template_name, context)