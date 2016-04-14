from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.utils.timesince import timesince

admin.autodiscover()
from django.views.generic.base import TemplateView
from gmaps.models import UbicacionForm, Ubicacion
import json
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

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^nueva/ubicacion/$', GuardarUbicacionView, name='guardar-ubicacion'),
    )
