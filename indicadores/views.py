from django.shortcuts import render, redirect
from django import views
from .models import Indicador, Evidencia
from django.db.models import Q
from .forms import UploadFileForm
from django.contrib.auth.models import User

class Dashboard(views.View):

    def get(self, request):
        template_name="indicadores/dashboard.html"

        if request.user.is_superuser:
            total = len(Indicador.objects.all())
            verde = len(Indicador.objects.filter(status="Satisfactorio"))
            amarillo = len(Indicador.objects.filter(status="Regular"))
            rojo = len(Indicador.objects.filter(status="Insatisfactorio"))
        else:
            total = len(Indicador.objects.filter(area=request.user))
            verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
            amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
            rojo = len(Indicador.objects.filter(area=request.user, status="Insatisfactorio"))
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
        rojo = len(Indicador.objects.filter(area=request.user, status="Insatisfactorio"))

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
        rojo = len(Indicador.objects.filter(area=request.user, status="Insatisfactorio"))

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
        rojo = len(Indicador.objects.filter(area=request.user, status="Insatisfactorio"))

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
        indicadores = Indicador.objects.filter(area=request.user, status="Insatisfactorio")

        if q:
            indicadores = Indicador.objects.filter(Q(area=request.user),
                                                   Q(status="Insatisfactorio"),
                                                   Q(nombre__icontains=q) |
                                                   Q(indicador__icontains=q) |
                                                   Q(descripcion__icontains=q)).distinct()


        total = len(Indicador.objects.filter(area=request.user))
        verde = len(Indicador.objects.filter(area=request.user, status="Satisfactorio"))
        amarillo = len(Indicador.objects.filter(area=request.user, status="Regular"))
        rojo = len(Indicador.objects.filter(area=request.user, status="Insatisfactorio"))

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
        form = UploadFileForm()
        context = {'indicador':indicador, 'form':form}

        return render(request, template_name, context)

    def post(self, request, pk):

        indicador = Indicador.objects.get(pk=pk)
        form = UploadFileForm(request.POST, request.FILES, instance=indicador)
        print(form)
        if form.is_valid():
            print("Valido")
            form_data = form.save(commit=False)
            print(form_data)
            form_data.save()
            return redirect('indicadores:detail', pk)
        else:
            return redirect('indicadores:list')



class EvidenciasDetailView(views.View):

    def get(self, request, pk, epk):

        template_name="indicadores/evidencia_detail.html"
        indicador = Indicador.objects.get(pk=pk)
        evidencia = Evidencia.objects.get(pk=epk, indicador=indicador)

        context = {'evidencia': evidencia}

        return render(request, template_name, context)


class ResumenAreaList(views.View):

    def get(self, request):

        template_name="indicadores/resumen/lista.html"
        q = request.GET.get('q')

        areas = User.objects.all()

        if q:
            areas = User.objects.filter(Q(username__icontains=q)|
                                        Q(first_name__icontains=q)|
                                        Q(last_name__icontains=q))

        context = {'areas': areas}

        return render(request, template_name, context)


class ResumenAreaDetail(views.View):
    pass


class ResumenGeneral(views.View):
    pass