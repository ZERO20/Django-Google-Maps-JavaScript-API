#encoding:utf-8
__author__ = 'edgar'
from django.forms import ModelForm
from django import forms
from  gmaps.models import Ubicacion

class UbicacionForm(ModelForm):
	class Meta:
		model = Ubicacion
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder':'Nombre de la ubicación'}),
			'lat': forms.TextInput(attrs={'placeholder':'Latitud'}),
			'lng': forms.TextInput(attrs={'placeholder':'Longitud'}),
			'user': forms.Select(attrs={'class':'select-select2 span12'}),
		}