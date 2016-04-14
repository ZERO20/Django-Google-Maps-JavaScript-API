from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from gmaps.models import Ubicacion
from gmaps.forms import UbicacionForm
from django.http import HttpResponse
from django.utils.timesince import timesince
import json
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        ubicaciones = Ubicacion.objects.all().order_by('-fecha')
        context["ubicaciones"] = ubicaciones
        context["form"] = UbicacionForm
        return context


def GuardarUbicacionView(request):
    if request.is_ajax():
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            ubicaciones = Ubicacion.objects.all().order_by('-fecha')
            data = '<ul id="ubicaciones">'
            print data
            for ubicacion in ubicaciones:
                data +='<li>%s %s -hace %s</li>'%(ubicacion.nombre,ubicacion.user,timesince(ubicacion.fecha))
            data += '</ul>'
            return HttpResponse(json.dumps({'ok':True,'msg':data}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'ok':False,'msg':'Debes completar los campos.'}),mimetype='application/json')


class ListaUbicacionesView(ListView):
    model = Ubicacion
    template_name = 'ubicacion_list.html'
    context_object_name = 'ubicaciones'


class DetalleUbicacionView(DetailView):
    model = Ubicacion
    context_object_name = 'ubicacion'
    template_name = 'ubicacion_detail.html'



