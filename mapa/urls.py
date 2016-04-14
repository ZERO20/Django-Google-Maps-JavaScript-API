from django.conf.urls import patterns, include, url
from django.contrib import admin
from gmaps.views import HomeView,GuardarUbicacionView,ListaUbicacionesView,DetalleUbicacionView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^nueva/ubicacion/$', GuardarUbicacionView, name='guardar-ubicacion'),
    url(r'^lista/ubicacion/$', ListaUbicacionesView.as_view(), name='lista-ubicacion'),
    url(r'^detalle/ubicacion/(?P<pk>\d+)/$', DetalleUbicacionView.as_view(), name='detalle-ubicacion'),
    )
